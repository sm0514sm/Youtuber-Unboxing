# -*- encoding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import threading
from datetime import datetime, timedelta
from dataServer.models import Youtuber
import time
from decouple import config
import urllib.request
import json
import pprint

key_list = [config('GOOGLEAPIKEY1'), config('GOOGLEAPIKEY2'),
            config('GOOGLEAPIKEY3'), config('GOOGLEAPIKEY4')]
key_index = 0


class updateThread:
    def __init__(self):
        pass

    def threadOpen(self):
        global key_index, key_list
        KEY = key_list[key_index]
        base_url = "https://www.googleapis.com/youtube/v3/channels"
        part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
        youtubers = Youtuber.objects.all()[:1]
        left_api_keys = len(key_list)
        for  youtuber in youtubers:
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
                return HttpResponse('key is expired.')  # api_key 모두 소진
            now = datetime.utcnow() + timedelta(hours=9)
            
            info_obj = json.loads(response.read().decode('utf-8')).get('items')[0]
            
            snippet = info_obj.get('snippet')
            statistics = info_obj.get('statistics')
            branding_settings = info_obj.get('brandingSettings')
            content_details = info_obj.get('contentDetails')
            
            # print(youtuber.yno, ' : ', youtuber.channelname)
            # youtuber.searchkeyword = 'test2'
            # youtuber.save()
            
            youtuber.channelname = snippet.get('title')
            youtuber.youtubername = snippet.get('customURL')
            youtuber.channeldescription = snippet.get('description')
            youtuber.bannerimagelink = branding_settings.get('image').get('bannerImageUrl')
            if '/default_banner' in youtuber.bannerimagelink:
                youtuber.bannerimagelink = ''
            youtuber.thumbnails = snippet.get('thumbnails').get('default')
            youtuber.subscriber = statistics.get('subscriberCount')  # 이건 트렌드에도 추가해야 됨
            youtuber.totalviewcount = statistics.get('viewCount')    # 이건 트렌드에도 추가해야 됨
            youtuber.totalvideocount = statistics.get('videoCount')
            youtuber.updateddate = '%d-%d-%d %d:%d:%d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
            youtuber.otherlink1 = other_links[0]
            youtuber.otherlink2 = other_links[1]
            youtuber.otherlink3 = other_links[2]
            youtuber.otherlink4 = other_links[3]
            youtuber.otherlink5 = other_links[4]
            youtuber.uploadsid = channel_info['uploadsID']
            
            
            # youtuber = Youtuber.objects.create(
            #     # channelid=channel_id,
            #     channelname=channel_info['title'],
            #     youtubername=channel_info['customUrl'],
            #     channeldescription=channel_info['description'],
            #     bannerimagelink=channel_info['banner_url'],
            #     # channellink=url,
            #     thumbnails=channel_info['thumbnail'],
            #     # publisheddate=channel_info['publishedAt'],
            #     subscriber=channel_info['subscriberCount'], # 이건 트렌드에도 추가해야 됨
            #     totalviewcount=channel_info['viewCount'], # 이것도 업데이트
            #     totalvideocount=channel_info['videoCount'], # 이것도 업데이트
            #     # grade='Unknown',
            #     # influence='0',
            #     # activity='0',
            #     # subscribercounttrend='0',
            #     # viewcounttrend='0',
            #     # charm='0',
            #     # clickcount='0',
            #     updateddate='%d-%d-%d %d:%d:%d' % (now.tm_year, now.tm_mon,
            #                                     now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),
            #     # regdate='%d-%d-%d' % (now.tm_year, now.tm_mon, now.tm_mday),
            #     otherlink1=other_links[0],
            #     otherlink2=other_links[1],
            #     otherlink3=other_links[2],
            #     otherlink4=other_links[3],
            #     otherlink5=other_links[4],
            #     uploadsid=channel_info['uploadsID']
            # )
            
            
        # threading.Timer(86000, self.threadOpen).start()

############## 서버 켜짐과 동시에 자동 업데이트를 실행하는 로직 ##############

def update_youtuber(request):
    updateStart = updateThread()
    updateStart.threadOpen()
    return HttpResponse()

now = datetime.utcnow() + timedelta(hours=9)


print('-----------------------------------')
print(now)
print('%d-%d-%d' % (now.year, now.month, now.day))
print('-----------------------------------')


