# -*- encoding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import threading
import datetime
from dataServer.models import Youtuber, Trend, Video
from dataServer.function import get_channel_other_sites
import time
from decouple import config
import urllib.request
import json
import pprint
from pytz import timezone, tzinfo
from django.utils import timezone

key_list = [config('GOOGLEAPIKEY5'), config('GOOGLEAPIKEY7'), config('GOOGLEAPIKEY6'), config('GOOGLEAPIKEY8'),
            config('GOOGLEAPIKEY1'), config('GOOGLEAPIKEY2'), config('GOOGLEAPIKEY3'), config('GOOGLEAPIKEY4'),
            config('GOOGLEAPIKEY9')]
key_index = 0


class updateThread:
    def __init__(self):
        pass

    def threadOpen(self):
        global key_index, key_list
        KEY = key_list[key_index]
        base_url = "https://www.googleapis.com/youtube/v3/channels"
        # part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
        part = "snippet,brandingSettings,contentDetails,statistics"
        youtubers = Youtuber.objects.all()[:1]
        left_api_keys = len(key_list)
        for  youtuber in youtubers:
            ## 날짜 비교해서 최신이면 그냥 넘어가는 로직도 만들자.
            ################## 유튜버 테이블 업데이트
            while left_api_keys:
                try:
                    response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, youtuber.channelid, KEY))
                    break
                except urllib.request.HTTPerror:
                    print('*--- next key setting ---*')
                    key_index += 1
                    key_index %= len(key_list)
                    left_api_keys -= 1
            if not left_api_keys:
                return HttpResponse('key is expired during updating Youtuber Page. {} is not updated.'.format(youtuber.yno))  # api_key 모두 소진
            
            info_obj = json.loads(response.read().decode('utf-8')).get('items')[0]
            
            snippet = info_obj.get('snippet')
            statistics = info_obj.get('statistics')
            branding_settings = info_obj.get('brandingSettings')
            content_details = info_obj.get('contentDetails')
            
            other_links = ['', '', '', '', '']
            for (i, site) in enumerate(get_channel_other_sites(youtuber.channellink)):
                other_links[i] = site
            
            now = datetime.datetime.now()
            
            youtuber.channelname = snippet.get('title')
            youtuber.youtubername = snippet.get('customURL')
            youtuber.channeldescription = snippet.get('description')
            youtuber.bannerimagelink = branding_settings.get('image').get('bannerImageUrl')
            if '/default_banner' in youtuber.bannerimagelink:
                youtuber.bannerimagelink = ''
            youtuber.thumbnails = snippet.get('thumbnails').get('default').get('url')
            youtuber.subscriber = statistics.get('subscriberCount')  # 이건 트렌드에도 추가해야 됨
            youtuber.totalviewcount = statistics.get('viewCount')    # 이건 트렌드에도 추가해야 됨
            youtuber.totalvideocount = statistics.get('videoCount')
            youtuber.updateddate = '{0:04d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
            youtuber.otherlink1 = other_links[0]
            youtuber.otherlink2 = other_links[1]
            youtuber.otherlink3 = other_links[2]
            youtuber.otherlink4 = other_links[3]
            youtuber.otherlink5 = other_links[4]
            youtuber.uploadsid = content_details.get('relatedPlaylists').get('uploads')
            
            youtuber.save()
            
            print("------------- Yno {}'s youtuber table is updated. -------------".format(youtuber.yno))
            
            ################## 트렌드 새로운 열 추가
            target_youtuber = Youtuber.objects.get(yno=youtuber.yno)
            
            last_trend = Trend.objects.all().filter(yno=youtuber).order_by('-recorddate')[0]
            last_date = last_trend.recorddate
            
            if last_date.day != now.day and last_date.month != now.month and last_date.year != now.year: 
                last_subscriber = last_trend.pointsubscriber
                last_pointview = last_trend.pointview
                
                new_trend = Trend.objects.create(
                    yno = target_youtuber,
                    recorddate = '{0:04d}-{1:02d}-{2:02d}'.format(now.year, now.month, now.day),
                    pointsubscriber = target_youtuber.subscriber,
                    difsubscriber = target_youtuber.subscriber - last_subscriber, # 이전 꺼 가져오기
                    pointview = target_youtuber.totalviewcount,
                    difview = target_youtuber.totalviewcount - last_pointview,
                )
                
                new_trend.save()
                
                print("------------- Yno {}'s trend table is updated. -------------".format(youtuber.yno))
            else:
                print("------------- Yno {}'s trend table is not updated since last update is duplicate. -------------".format(youtuber.yno))
            
            ################## 새로운 영상들 가져오기
            base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
            upload_id = youtuber.uploadsid
            while left_api_keys:
                try:
                    max_result = 50
                    response = urllib.request.urlopen(base_url + "?playlistId={}&key={}&part=snippet&maxResults={}".format(upload_id, KEY, max_result))
                    break
                except urllib.request.HTTPerror:
                    print('*--- next key setting ---*')
                    key_index += 1
                    key_index %= len(key_list)
                    left_api_keys -= 1
            if not left_api_keys:
                return HttpResponse('key is expired during updating latest videos. {} is not updated.'.format(youtuber.yno))
            
            new_videos = []
            latest_videos = json.loads(response.read().decode('utf-8')).get('items')
            youtuber_videos = Video.objects.all().filter(yno=youtuber).order_by('-regdate')
            for video in latest_videos:
                snippet = video.get('snippet')
                videoID = snippet.get('resourceId').get('videoId')
                
            
            
        ########## 모두 끝나고, 업데이트 주기 다시 실행!
        # threading.Timer(86000, self.threadOpen).start()
        

def update_youtuber(request):
    updateStart = updateThread()
    updateStart.threadOpen()
    return HttpResponse()


# 어웨어와 나이브의 문제. 중요한 문제

youtuber_videos = Video.objects.all().filter(yno=545).order_by('-regdate')
for a in youtuber_videos:
    print(a.regdate)



# with open("test.json", 'w', encoding='utf-8-sig') as file:
#     json.dump(info_obj, file, indent="\t", ensure_ascii=False)