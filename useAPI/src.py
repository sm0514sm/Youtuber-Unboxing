from urllib.request import urlopen
from bs4 import BeautifulSoup

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