from urllib.request import Request, urlopen
import requests
import sys
import io
from bs4 import BeautifulSoup as BS

input_URL = 'https://www.youtube.com/channel/UCwx6n_4OcLgzAGdty0RWCoA'
URL = input_URL

html = urlopen(URL).read()
soup = BS(html, "html.parser", from_encoding='utf-8')
ff = soup.find_all("button", attrs={'class':"yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer"})
youtubeID = ff[0].get('data-channel-external-id')
print(youtubeID)