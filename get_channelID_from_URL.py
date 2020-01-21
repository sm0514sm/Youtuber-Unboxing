from urllib.request import urlopen
from bs4 import BeautifulSoup

input_URL = 'https://www.youtube.com/channel/UCYgUhR7EGKauFXgJS0pckGg/playlists'

URL = input_URL

html = urlopen(URL).read()
page_obj = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
class_attr = "yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer"
channelID = page_obj.find(
    "button", 
    attrs = {
            'class': class_attr 
        }).get('data-channel-external-id')

print(channelID)