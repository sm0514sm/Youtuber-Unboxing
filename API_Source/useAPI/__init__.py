from urllib.request import urlopen
from bs4 import BeautifulSoup
from decouple import config
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