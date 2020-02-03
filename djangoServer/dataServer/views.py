from django.shortcuts import render, HttpResponse
from .models import *
import urllib.request
import time
from decouple import config
from urllib.request import urlopen, unquote
from bs4 import BeautifulSoup as bs
import json
import copy
import timeit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
    start = timeit.default_timer()
    key_google = config('GOOGLEAPIKEY')
    url = url.replace('~', '/')

    # 1. 올바른 유튜브 채널 URL 판단
    if not is_youtube_channel_url(url):
        return HttpResponse(-1)
    end1 = timeit.default_timer() - start
    print('1. Determine the correct YouTube channel URL : %.2fs' % end1)

    # 2. URL로부터 channel ID 얻기
    channel_id = get_channel_id_from_url(url)
    end2 = timeit.default_timer() - end1
    print('2. Get channel ID from URL : %.2fs' % end2)

    # 3. url 채널 정보가 DB에 없는지 판단
    yno = get_yno_from_channel_id(channel_id)
    if yno != -1:
        return HttpResponse(yno)
    end3 = timeit.default_timer() - end2
    print('3. Determines if channel information is not in the DB : %.2fs' % end3)

    # 4. 유튜버 channel info 수집 후 DB 추가
    now = time.gmtime(time.time())
    other_links = ['', '', '', '', '']
    for (i, site) in enumerate(get_channel_other_sites(url)):
        other_links[i] = site
    channel_info = get_channel_info(key_google, channel_id)
    if int(channel_info['subscriberCount']) < int(config('MIN_SUBSCRIBER')):
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
        uploadsid=channel_info['uploadsID']
    )
    youtuber.save()
    end4 = timeit.default_timer() - end3
    print('4. Add DB after collecting YouTube channel info : %.2fs' % end4)

    # 5. 생성된 유튜버의 yno를 DB에서 찾아 가져오기
    yno = get_yno_from_channel_id(channel_id)
    end5 = timeit.default_timer() - end4
    print('5. Locate and import the yno of the created user from the DB : %.2fs' % end5)

    # 6. Video 테이블 수집
    video_id_list = get_video_list(key_google, channel_info['uploadsID'])
    end66 = timeit.default_timer() - end5
    print('6. get video list : %.2fs' % end66)

    for video_id in video_id_list:
        video_detail = get_video_detail(video_id)
        end666 = timeit.default_timer() - end66
        print('666. get_video_detail : %.2fs' % end666)
        video = Video.objects.create(
            yno=youtuber,
            videoid=video_detail['video_id'],
            videoname=video_detail['videoName'],
            videodescription=video_detail['videoDescription'],
            videoviewcount=video_detail['videoViewCount'],
            videocommentcount=video_detail['videoCommentCount'],
            good=video_detail['good'],
            bad=video_detail['bad'],
            regdate=video_detail['regDate'],
            # ycano=video_detail['ycano'],
            tags=video_detail['tags'],
            thumbnail=video_detail['thumbnail'],
            topic=video_detail['topic'],
        )
        video.save()
    end6 = timeit.default_timer() - end5
    print('6. get & insert Video : %.2fs' % end6)

    # 7. Growth 테이블 수집
    growth_list = get_growth_list(channel_id)
    for growth_item in growth_list:
        growth = Growth.objects.create(
            yno=youtuber,
            recorddate=growth_item['fields']['recordDate'],
            pointsubscriber=growth_item['fields']['pointSubscriber'],
            difsubscriber=growth_item['fields']['difSubscriber'],
            pointview=growth_item['fields']['pointView'],
            difview=growth_item['fields']['difView']
        )
        growth.save()
    end7 = timeit.default_timer() - end6
    print('7. get & insert Growth : %.2fs' % end7)

    # Todo 8.  category_youtuber_relation, community_youtuber_relation, news 테이블 수집 후 DB 추가

    # Todo 9. 위에서 생성된 정보들 기반으로 스텟, 등급 계산

    # Todo 10. 유튜버의 스텟, 등급, updatedDate 갱신

    end = timeit.default_timer() - start
    print('*** total : %.2fs ***' % end)
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
    info_obj = json_obj["items"][0]

    snippet = info_obj["snippet"]
    channel_info_dict["title"] = snippet["title"]
    channel_info_dict['customUrl'] = snippet.get('customUrl')
    channel_info_dict["description"] = snippet["description"]
    channel_info_dict["thumbnail"] = snippet["thumbnails"]["default"]["url"]
    channel_info_dict['publishedAt'] = snippet["publishedAt"][:10]

    statistics = info_obj["statistics"]
    channel_info_dict["viewCount"] = statistics["viewCount"]
    channel_info_dict["subscriberCount"] = statistics["subscriberCount"]
    channel_info_dict["videoCount"] = statistics["videoCount"]

    branding_settings = info_obj["brandingSettings"]
    channel_info_dict['banner_url'] = branding_settings["image"]["bannerImageUrl"]
    if '/default_banner' in channel_info_dict['banner_url']:
        channel_info_dict['banner_url'] = ''

    content_details = info_obj['contentDetails']
    channel_info_dict['uploadsID'] = content_details['relatedPlaylists']['uploads']
    return channel_info_dict


def get_growth_list(channel_id):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    driver = webdriver.Chrome('./chromedriver', options=options)

    url = 'https://socialblade.com/youtube/channel/' + channel_id + '/monthly'
    driver.get(url)
    el = '//*[@id="socialblade-user-content"]'
    orm = []
    try:
        content = driver.find_element_by_xpath(el).text.split('\n')
        cnt = 0
        flag = False
        pk = 0
        data = dict()
        for line in content:
            if line == 'ESTIMATED EARNINGS':
                flag = True
                continue
            elif line == 'Daily Averages':
                break
            if flag:
                if cnt == 1:
                    cnt += 1
                    continue
                if cnt == 6:
                    fin = dict()
                    fin['pk'] = pk
                    pk += 1
                    fin['model'] = "dataServer.growth"
                    fin['fields'] = data
                    temp = copy.deepcopy(fin)
                    orm.append(temp)
                    cnt = 0
                    continue
                elif cnt == 0:
                    data['recordDate'] = line
                    cnt += 1
                else:
                    x = line.replace('+', "").replace(",", "").replace('--', '0').replace('LIVE', '')
                    total_stars = 0
                    if 'K' in x:
                        if len(x) > 1:
                            total_stars = float(x.replace('K', '')) * 1000  # convert k to a thousand
                    elif 'M' in x:
                        if len(x) > 1:
                            total_stars = float(x.replace('M', '')) * 1000000  # convert M to a million
                    else:
                        total_stars = int(x)  # Less than 1000
                    if cnt == 2:
                        data['difSubscriber'] = int(total_stars)
                    elif cnt == 3:
                        data['pointSubscriber'] = int(total_stars)
                    elif cnt == 4:
                        data['difView'] = int(total_stars)
                    elif cnt == 5:
                        data['pointView'] = int(total_stars)
                    cnt += 1
    except NoSuchElementException:
        pass
    driver.close()
    return orm


def get_video_list(key, uploads_id):
    video_id_lists = []
    page_token = ''
    base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
    while True:
        url = base_url + "?playlistId=%s&key=%s&part=snippet&maxResults=50" % (uploads_id, key)
        if page_token != '':
            url += "&pageToken=" + page_token
        response = urllib.request.urlopen(url)
        string = response.read().decode('utf-8')
        json_objs = json.loads(string)
        for obj in json_objs['items']:
            video_id_lists.append(obj['snippet']['resourceId']['videoId'])
        #     pageToken
        if json_objs.get('nextPageToken') is None or json_objs.get('nextPageToken') == '':
            break
        page_token = json_objs.get('nextPageToken')
    return video_id_lists


TOPICS = {
    '/m/04rlf': 'Music',
    '/m/05fw6t': "Children's music",
    '/m/02mscn': 'Christian music',
    '/m/0ggq0m': 'Classical music',
    '/m/01lyv': 'Country',
    '/m/02lkt': 'Electronic music',
    '/m/0glt670': 'Hip hop music',
    '/m/05rwpb': 'Independent music',
    '/m/03_d0': 'Jazz',
    '/m/028sqc': 'Music of Asia',
    '/m/0g293': 'Music of Latin America',
    '/m/064t9': 'Pop music',
    '/m/06cqb': 'Reggae',
    '/m/06j6l': 'Rhythm and blues',
    '/m/06by7': 'Rock music',
    '/m/0gywn': 'Soul music',
    '/m/0bzvm2': 'Gaming',
    '/m/025zzc': 'Action game',
    '/m/02ntfj': 'Action-adventure game',
    '/m/0b1vjn': 'Casual game',
    '/m/02hygl': 'Music video game',
    '/m/04q1x3q': 'Puzzle video game',
    '/m/01sjng': 'Racing video game',
    '/m/0403l3g': 'Role-playing video game',
    '/m/021bp2': 'Simulation video game',
    '/m/022dc6': 'Sports game',
    '/m/03hf_rm': 'Strategy video game',
    '/m/06ntj': 'Sports',
    '/m/0jm_': 'American football',
    '/m/018jz': 'Baseball',
    '/m/018w8': 'Basketball',
    '/m/01cgz': 'Boxing',
    '/m/09xp_': 'Cricket',
    '/m/02vx4': 'Football',
    '/m/037hz': 'Golf',
    '/m/03tmr': 'Ice hockey',
    '/m/01h7lh': 'Mixed martial arts',
    '/m/0410tth': 'Motorsport',
    '/m/066wd': 'Professional wrestling',
    '/m/07bs0': 'Tennis',
    '/m/07_53': 'Volleyball',
    '/m/02jjt': 'Entertainment',
    '/m/095bb': 'Animated cartoon',
    '/m/09kqc': 'Humor',
    '/m/02vxn': 'Movies',
    '/m/05qjc': 'Performing arts',
    '/m/019_rr': 'Lifestyle',
    '/m/032tl': 'Fashion',
    '/m/027x7n': 'Fitness',
    '/m/02wbm': 'Food',
    '/m/0kt51': 'Health',
    '/m/03glg': 'Hobby',
    '/m/068hy': 'Pets',
    '/m/041xxh': 'Physical attractiveness [Beauty]',
    '/m/07c1v': 'Technology',
    '/m/07bxq': 'Tourism',
    '/m/07yv9': 'Vehicles',
    '/m/01k8wb': 'Knowledge',
    '/m/098wr': 'Society',
}


def get_video_detail(video_id):
    # snippet으로 가져오는 정보: 유튜버, 제목, 설명, 게시일, 카테고리, 태그, 섬네일
    # statistics로 가져오는 정보: 조회수, 댓글 수, 좋아요 수, 싫어요 수
    # topicdetails로 가져오는 정보: 토픽
    part = 'snippet,statistics,topicDetails'
    url = 'https://www.googleapis.com/youtube/v3/videos?part={}&id={}&key={}'.format(part, video_id, config('GOOGLEAPIKEY'))
    response = urlopen(url).read().decode('utf-8')
    res_dict = json.loads(response).get('items')[0]

    topic = []
    topic_details = res_dict.get('topicDetails')
    statistics = res_dict.get('statistics')
    snippet = res_dict.get('snippet')
    if topic_details:
        topic_id = topic_details.get('topicIds')
        if topic_id:
            topic += topic_id
        relevant_topic_id = topic_details.get('relevantTopicIds')
        if relevant_topic_id:
            topic += relevant_topic_id

    topic = list(set(topic))

    topic_result = []
    for result in topic:
        topic_result.append(TOPICS.get(result))

    try:
        tags = ','.join(snippet.get('tags'))
    except:
        tags = ''

    try:
        topic = ','.join(topic_result)
    except:
        topic = ''
    if statistics.get('likeCount') is None:
        statistics['likeCount'] = -1
    if statistics.get('dislikeCount') is None:
        statistics['dislikeCount'] = -1
    if statistics.get('commentCount') is None:
        statistics['commentCount'] = -1
    video = {
        'video_id': video_id,
        'videoName': res_dict.get('snippet').get('title'),
        'videoDescription': snippet.get('description'),
        'videoViewCount': statistics.get('viewCount'),
        'videoCommentCount': statistics.get('commentCount'),
        'good': statistics.get('likeCount'),
        'bad': statistics.get('dislikeCount'),
        'regDate': snippet.get('publishedAt')[:10],
        'ycano': snippet.get('categoryId'),
        'thumbnail': snippet.get('thumbnails').get('high').get('url'),
        'tags': tags,
        'topic': topic,
    }

    # 파일 출력
    # PATH = 'videoTableTest.json'
    # with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file:
    #     json.dump(video, file, indent="\t", ensure_ascii=False)

    return video


def update_youtuber(request, yno):
    return HttpResponse(yno)


def add_video(request, videoId):
    pass

