from bs4 import BeautifulSoup
from decouple import config
from urllib.request import urlopen, unquote
from bs4 import BeautifulSoup as BS


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
    # 예시 채널 ID
    # channelID = 'UCUpJs89fSBXNolQGOYKn0YQ'
    KEY = config('GOOGLEAPIKEY')
    URL = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(KEY, channelID, maxResult)
    response = urlopen(URL).read().decode('utf8')
    # response에 str 타입으로 자료가 넘어옴


def get_channel_other_sites(input_url):
    html = urlopen(input_url).read()
    soup = BS(html, "html.parser", from_encoding='utf-8')
    ff = soup.find_all("button", attrs={'class': "yt-uix-button yt-uix-button-size-default "
                                                 "yt-uix-button-subscribe-branded yt-uix-button-has-icon "
                                                 "no-icon-markup yt-uix-subscription-button yt-can-buffer"})
    youtube_id = ff[0].get('data-channel-external-id')
    print(youtube_id)

    li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
    for li_tag in li_tags:
        before_link = li_tag.find('a').get('href')
        link = unquote(before_link[before_link.find('http'):])
        if '&' in link:
            link = link[:link.find('&')]
        print(link)


# response = requests.get(URL).text


print(type(response))
print(response)