 # -*- encoding: utf-8 -*-
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
    'page': 1,
    'size': 30,
}

headers = {
    'Authorization': 'KakaoAK ' + API_KEY,
}

URL = 'https://dapi.kakao.com/v2/search/cafe'

response = requests.get(URL, headers=headers, params=params)
res = json.loads(response.text)

keywords = ['유튜브', '유튜버', '채널', '유튭']

DB_list = []
documents = res.get('documents')
if (response.status_code == 200):
    for document in documents:
        try:
            contents = document.get('contents')
            for keyword in keywords:
                if keyword in contents:
                    new_rows = {
                        'yno': youtuber,
                        'articleTitle': document.get('title'),
                        'articleLink': document.get('url'),
                        'articleDescription': document.get('contents'),
                        'articleDate': document.get('datetime')[:10],
                    }
                    # pprint(new_rows)
                    DB_list.append(new_rows)
                    break
        except:
            print('error')
            continue
    # 날짜까지 계산
    print(DB_list)
    # PATH = 'daumCafeExample.json'
    # with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file:
    #     json.dump(DB_list, file, indent="\t", ensure_ascii=False)
else:
    print('error code : ' + response.status_code)
    
    
# PATH = 'daumCafeExample.json'
# with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file:
#     json.dump(res, file, indent="\t", ensure_ascii=False)
print('\U0001F61A')