import json
import requests
from decouple import config
import datetime

# 네이버 카페는 날짜를 주지 않는 관계로 

YOUTUBER = '피지컬갤러리'

NECESSARY_WORD = [
    ['유튜브', '유튜버', '유투버', '채널'], # 기본
    ['게임', 'game'], # 게임
    ['엔터테인먼트', '예능', 'entertainment'], # 엔터테인먼트
    ['뷰티', '화장', '패션'], # 뷰티
    ['운동', 'Sports', '스포츠', '헬스', '피트니스'], # 스포츠
    ['먹방', '음식', '푸드', 'Food'], # 먹방
    ['키즈', '어린이', 'Kids'], # 키즈
    ['동물', '애니멀', 'Animal'], # 동물
    ['일상', '브이로그', 'V-log', 'Vlog'], # 일상
    ['IT', 'SW', '소프트웨어', '기술', '신제품', '노트북', '컴퓨터', '시스템', '스마트폰', '무선', '과학'] # IT
]

BLOG_URL = 'https://openapi.naver.com/v1/search/blog.json?'
CAFE_URL = 'https://openapi.naver.com/v1/search/cafearticle.json?'

cafeURL = CAFE_URL
blogURL = BLOG_URL

params = {
    'query': YOUTUBER,
    'display': 100,  # 10 ~ 100
    'start': 1,     # 1 ~ 1000
    'sort': 'date'  # sim : 유사도순, date: 날짜순
}

headers = {
    'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
    'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
}

response = json.loads(requests.get(cafeURL, params=params, headers=headers).text)

items = response["items"] # list

youtuber = 12 # 유튜버 정보를 가져온다.

newsColumns = {
    'yno': youtuber,
    'newsLink': '',
    'newsTitle': '',
    'newsDescription': '',
    'newsDate': '',
    'pressName': '',
    ''
}

category_keyword = NECESSARY_WORD[0]
for num in CATEGORY:
    category_keyword += NECESSARY_WORD[num]


## 유니크한 건 최신 날짜?
## 카페글은 없어지기도 함... 없어지는 글에 대해 처리하자.

# 만약 last updatedDate 가 2019-03-15 면 3월 15일 이후의 기사만 가져와야함
updatedDate = datetime.datetime(2019, 3, 15)

while True:
    response = requests.get(URL, params=params, headers=headers).text  # str type
    total = json.loads(response)["total"]
    newses = json.loads(response)["items"]
    

    for index, news in enumerate(newses):
        isCorrect = False
        date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(news["pubDate"][8:11]), int(news["pubDate"][5:7]))

#         # 업데이트되어있는 기사는 추가하지 않음
#         if (date - updatedDate).days < 0:
#             break

#         # Description 에 특정 키워드가 없는 기사는 추가하지 않음
#         for keyword in category_keyword:
#             if keyword in news["description"]:
#                 isCorrect = True
#                 break
#         if not isCorrect:
#             continue

#         newNews = {
#             'newsLink': news["link"],
#             'newsTitle': news["title"],
#             'newsDescription': news["description"],
#             'newsDate': str(date)[:10]
#         }
#         print(newNews)
#     if params['start'] >= min(200, total):
#         break
#     params['start'] += params['display']


# PATH = '피지컬갤러리_naverCafe결과.json'
# with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file:
#     json.dump(json.loads(response), file, indent="\t", ensure_ascii=False)