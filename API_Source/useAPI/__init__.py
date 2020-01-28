from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as BS
from decouple import config
from urllib.request import urlopen, unquote
import urllib.request
import json
import sys
import io

############### print 할 때 utf-8 디코딩이 안 될 경우 주석 해제
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def get_channelID_from_URL(input_URL):
    # 해당 유튜버 페이지의 버튼 태그에서 속성값을 가져온다.
    html = urlopen(input_URL).read()
    page_obj = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    class_attr = "yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer"
    channelID = page_obj.find(
        "button", 
        attrs = {
                'class': class_attr 
            }).get('data-channel-external-id')

    return channelID

def get_latest_videos_using_channelID(channelID):
    KEY = config('GOOGLEAPIKEY')
    URL = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(KEY, channelID, maxResult)
    response = urlopen(URL).read().decode('utf8')
    
    # response에 str 타입으로 자료가 넘어옴
    # response = requests.get(URL).text
    
    print(type(response))
    print(response)
    


def get_video_details(videoID):
    URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key={}'.format(videoID, config('GOOGLEAPIKEY'))
    response = urlopen(URL).read().decode('utf-8')
    res_dict = json.loads(response)
    # print(response)
    # 들어온 정보를 JSON으로 저장
    PATH = 'zzzz.json'
    with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file:
        json.dump(res_dict, file, indent="\t", ensure_ascii=False)


def get_channel_other_sites(input_url):
    other_link_list = []
    html = urlopen(input_url).read()
    soup = BS(html, "html.parser", from_encoding='utf-8')
    li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
    for li_tag in li_tags:
        before_link = li_tag.find('a').get('href')
        link = unquote(before_link[before_link.find('http'):])
        if '&' in link:
            link = link[:link.find('&')]
        other_link_list.append(link)
    return other_link_list


def get_channel_info(channelID):
    channel_info_dict = {}
    base_url = "https://www.googleapis.com/youtube/v3/channels"
    part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
    response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, channelID, key))
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    snippet = json_obj["items"][0]["snippet"]
    title = snippet["title"]
    description = snippet["description"]
    thumbnail = snippet["thumbnails"]["default"]["url"]
    channel_info_dict["title"] = title
    channel_info_dict["description"] = description
    channel_info_dict["thumbnail"] = thumbnail

    statistics = json_obj["items"][0]["statistics"]
    view_count = statistics["viewCount"]
    subscriber_count = statistics["subscriberCount"]
    video_count = statistics["videoCount"]
    channel_info_dict["viewCount"] = view_count
    channel_info_dict["subscriberCount"] = subscriber_count
    channel_info_dict["videoCount"] = video_count

    return channel_info_dict


if __name__ == "__main__":
    key = config('GOOGLEAPIKEY')

    url = "https://www.youtube.com/user/officialpsy"
    channel_id = get_channelID_from_URL(url)
    # get_latest_videos_using_channelID(channel_id)
    other_links = get_channel_other_sites(url)
    channel_info = get_channel_info(channel_id)


    print('* url : ' + url)
    print('* channel_id : ' + channel_id)
    print('* other_links : ' + str(len(other_links)))
    for index, link in enumerate(other_links):
        print('\t%d - %s' %(index + 1, link))
    print('* channel_info')
    for item in channel_info:
        print('\t%s - %s' %(item, channel_info[item]))
