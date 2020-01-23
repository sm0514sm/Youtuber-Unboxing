from urllib.request import Request, urlopen
import requests
import sys
import io
from bs4 import BeautifulSoup as BS

# 이건 됐다.


# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

input_URL = 'https://www.youtube.com/channel/UCwx6n_4OcLgzAGdty0RWCoA'
URL = input_URL

html = urlopen(URL).read()
soup = BS(html, "html.parser", from_encoding='utf-8')
ff = soup.find_all("button", attrs={'class':"yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer"})
youtubeID = ff[0].get('data-channel-external-id')
print(youtubeID)
# for f in ff:
#     print(f)

# print(soup)


# print(type(html))
# print(html)
# # URL = 'https://www.naver.com/'

# response = requests.get(URL)
# print(type(response))
# # print(dir(response))
# print(type(response))
# with open('test.json', 'w', encoding='utf-8') as file:
#     file.write(response)

# print(bs)