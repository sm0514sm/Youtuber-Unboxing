import urllib.request
from decouple import config
import json
import requests
from pprint import pprint


API_KEY = config('DAUM_API_KEY')
youtuber = 7 # 유튜버 고유번호


params = {
    'query': '피지컬갤러리',
    'sort': 'recency',
    'page': '1',
    'size': '10',
}

headers = {
    'Authorization': 'KakaoAK ' + API_KEY,
}

URL = 'https://dapi.kakao.com/v2/search/cafe'

response = requests.get(URL, headers=headers, params=params)
res = json.loads(response.text)
data = res.gt('documents')

keywords = ['유튜브', '유튜버', '채널']

new_rows = {
    'yno': youtuber,
    'articleTitle': '',
    'articleLink': '',
    'articleDescription': '',
    'articleDate': '',
    'communityName': '',
}

DB_list = []


if (response.status_code == 200):
    new_rows = {
        'yno': youtuber,
        'articleTitle': '',
        'articleLink': '',
        'articleDescription': '',
        'articleDate': '',
        'communityName': '',
    }
    # pprint(res)
else:
    print('error code : ' + response.status_code)
    
    
# PATH = 'daumCafeExample.json'
# with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
#     json.dump(res, file, indent="\t", ensure_ascii=False)