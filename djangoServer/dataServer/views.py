from django.shortcuts import render, HttpResponse
from .models import *
import urllib.request
import json
import time
from decouple import config
from urllib.request import urlopen, unquote
from bs4 import BeautifulSoup as bs

# Create your views here.
text = ""


def index(request):
    return HttpResponse(Youtuber.objects.all()[0].youtubername)


'''
## return 값 ## 
>   0, DB에 존재하는 유튜버 url을 입력받아서 해당 유튜버의 yno를 반환
=   0, 성공적으로 성공함
=  -1, 올바르지 않은 유튜브 채널 URL인 경우
=  -3, url 채널 정보가 DB에 없는지 판단 중 에러
=  -4, 유튜버 channel info 수집 후 DB 추가 중 에러
=  -5. 생성된 유튜버의 yno를 DB에서 찾아 가져오기 중 에러
=  -6. 다른 기타 정보 테이블 수집 후 DB 추가 중 에러
=  -7. 위에서 생성된 정보들 기반으로 스텟, 등급 계산 중 에러
=  -8. 유튜버의 스텟, 등급, updatedDate 갱신 중 에러 
= -10, 알 수 없는 오류
= -11, 너무 인기 없는 유튜버라서 지원안함'''


def make_new_youtuber(request, url):
    key_google = config('GOOGLEAPIKEY')
    url = url.replace('~', '/')

    # 1. 올바른 유튜브 채널 URL 판단
    if not is_youtube_channel_url(url):
        return HttpResponse(-1)

    # 2. URL로부터 channel ID 얻기
    channel_id = get_channel_id_from_url(url)

    # 3. url 채널 정보가 DB에 없는지 판단
    yno = get_yno_from_channel_id(channel_id)
    if yno != -1:
        return HttpResponse(yno)

    # 4. 유튜버 channel info 수집 후 DB 추가
    now = time.gmtime(time.time())
    other_links = ['', '', '', '', '']
    for (i, site) in enumerate(get_channel_other_sites(url)):
        other_links[i] = site
    channel_info = get_channel_info(key_google, channel_id)
    if channel_info['subscriberCount'] < config('MIN_SUBSCRIBER'):
        return HttpResponse(-11)
    youtuber = Youtuber.objects.create(
        channelid=channel_id,
        channelname=channel_info['title'],
        youtubername=channel_info['customUrl'],
        channeldescription=channel_info['description'],
        bannerimagelink=channel_info['banner_url'],
        channellink=url,
        thumbnails=channel_info['thumbnail'],
        publisheddate=channel_info['publishedAt'],
        subscriber=channel_info['subscriberCount'],
        totalviewcount=channel_info['viewCount'],
        totalvideocount=channel_info['videoCount'],
        grade='Unknown',
        influence='0',
        activity='0',
        growth='0',
        basicstat='0',
        charm='0',
        clickcount='0',
        updateddate='%d-%d-%d %d:%d:%d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),
        regdate='%d-%d-%d' % (now.tm_year, now.tm_mon, now.tm_mday),
        otherlink1=other_links[0],
        otherlink2=other_links[1],
        otherlink3=other_links[2],
        otherlink4=other_links[3],
        otherlink5=other_links[4],
    )
    youtuber.save()

    # 5. 생성된 유튜버의 yno를 DB에서 찾아 가져오기
    yno = get_yno_from_channel_id(channel_id)

    # Todo 6. video, category_youtuber_relation, community_youtuber_relation, growth, news 테이블 수집 후 DB 추가
    # Todo 7. 위에서 생성된 정보들 기반으로 스텟, 등급 계산
    # Todo 8. 유튜버의 스텟, 등급, updatedDate 갱신
    return HttpResponse(0)


def is_youtube_channel_url(url):
    if 'youtube' not in url:
        return False
    if '/c/' not in url and '/user/' not in url and '/channel/' not in url:
        return False
    return True


def get_channel_id_from_url(url):
    html = urlopen(url).read()
    soup = bs(html, "html.parser", from_encoding='utf-8')
    ff = soup.find("button", attrs={'class': "yt-uix-button yt-uix-button-size-default "
                                                 "yt-uix-button-subscribe-branded yt-uix-button-has-icon "
                                                 "no-icon-markup yt-uix-subscription-button yt-can-buffer"})
    return ff.get('data-channel-external-id')


def get_yno_from_channel_id(channel_id):
    global text
    for youtuber in Youtuber.objects.all():
        if channel_id == youtuber.channelid:
            return youtuber.yno
    return -1


def get_channel_other_sites(input_url):
    other_link_list = []
    html = urlopen(input_url).read()
    soup = bs(html, "html.parser", from_encoding='utf-8')
    li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
    for li_tag in li_tags:
        before_link = li_tag.find('a').get('href')
        link = unquote(before_link[before_link.find('http'):])
        if '&' in link:
            link = link[:link.find('&')]
        other_link_list.append(link)
    return other_link_list


def get_channel_info(key, channelID):
    channel_info_dict = {}
    base_url = "https://www.googleapis.com/youtube/v3/channels"
    part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
    response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, channelID, key))
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    snippet = json_obj["items"][0]["snippet"]
    channel_info_dict["title"] = snippet["title"]
    channel_info_dict['customUrl'] = snippet.get('customUrl')
    channel_info_dict["description"] = snippet["description"]
    channel_info_dict["thumbnail"] = snippet["thumbnails"]["default"]["url"]
    channel_info_dict['publishedAt'] = snippet["publishedAt"][:10]

    statistics = json_obj["items"][0]["statistics"]
    channel_info_dict["viewCount"] = statistics["viewCount"]
    channel_info_dict["subscriberCount"] = statistics["subscriberCount"]
    channel_info_dict["videoCount"] = statistics["videoCount"]

    branding_settings = json_obj["items"][0]["brandingSettings"]
    channel_info_dict['banner_url'] = branding_settings["image"]["bannerImageUrl"]

    return channel_info_dict


def update_youtuber(request, yno):
    return HttpResponse(yno)


if __name__ == "__main__":
    pass

def add_video(request, videoId):
    pass

