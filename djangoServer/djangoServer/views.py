# -*- encoding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import threading
from datetime import datetime, timedelta
from dataServer.models import Youtuber
from dataServer.function import get_channel_other_sites
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
        # 안 쓰는 파트 나중에 삭제하자
        part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
        youtubers = Youtuber.objects.all()[8:11]
        left_api_keys = len(key_list)
        for  youtuber in youtubers:
            
            # 유튜버 테이블 업데이트
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
            
            now = datetime.utcnow() + timedelta(hours=9)
            
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
            
            print("{}: {}'s youtuber table is updated.".format(youtuber.yno, 1))
            
            
            
            
            # youtuber.save() # 여기까지 끝나면 일단 유튜버 정보는 업데이트 성공!
            
        
        ########## 모두 끝나고, 업데이트 주기 다시 실행!
        # threading.Timer(86000, self.threadOpen).start()
        

def update_youtuber(request):
    updateStart = updateThread()
    updateStart.threadOpen()
    return HttpResponse()


