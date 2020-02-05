import json
import requests
from decouple import config
import datetime

# 기본, 게임, 엔터테인먼트, 뷰티, 스포츠, 먹방, 키즈, 동물, 일상, IT
NECESSARY_WORD = [
    ['유튜브', '유튜버', '유투버', '채널'], # 기본
    ['게임', 'game'], # 게임
    ['엔터테인먼트', '예능', 'entertainment'], # 엔터테인먼트
    ['뷰티', '화장', '패션'], # 뷰티
    ['운동', 'Sports', '스포츠', '헬스'], # 스포츠
    ['먹방', '음식', '푸드', 'Food'], # 먹방
    ['키즈', '어린이', 'Kids'], # 키즈
    ['동물', '애니멀', 'Animal'], # 동물
    ['일상', '브이로그', 'V-log', 'Vlog'], # 일상
    ['IT', 'SW', '소프트웨어', '기술', '신제품', '노트북', '컴퓨터', '시스템', '스마트폰', '무선'] # IT
]

MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
YOUTUBER = 'workman'    # DB 에서 yno 에 해당하는 channelName or youtubeName 을 입력
CATEGORY = [2]     # 해당 유튜버의 카테고리가 게임과 엔터테인먼트

NEWS_URL = 'https://openapi.naver.com/v1/search/news.json?'
BLOG_URL = 'https://openapi.naver.com/v1/search/blog.json?'
CAFE_URL = 'https://openapi.naver.com/v1/search/cafearticle.json?'

URL = NEWS_URL

params = {
    'query': YOUTUBER,
    'display': 100,  # 10 ~ 100
    'start': 1,  # 1 ~ 1000
    'sort': 'date' # sim 유사도순, date 날짜순
}


headers = {
    'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
    'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
}

category_keyword = NECESSARY_WORD[0]

for num in CATEGORY:
    category_keyword += NECESSARY_WORD[num]

# print('Category Keywords:', category_keyword)

# 만약 last updatedDate 가 2019-03-15 면 3월 15일 이후의 기사만 가져와야함
updatedDate = datetime.datetime(2019, 3, 15)

while True:
    response = requests.get(URL, params=params, headers=headers).text  # str type
    total = json.loads(response)["total"]
    newses = json.loads(response)["items"]

############# 파일로 출력
##### with open("work_getNaverNews.json", 'w', encoding='utf-8-sig') as file: 
#####     json.dump(json.loads(response), file, indent="\t", ensure_ascii=False)

    for (index, news) in enumerate(newses):
        isCorrect = False
        date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(news["pubDate"][8:11]), int(news["pubDate"][5:7]))

        # 업데이트되어있는 기사는 추가하지 않음
        if (date - updatedDate).days < 0:
            break

        # Description 에 특정 키워드가 없는 기사는 추가하지 않음
        for keyword in category_keyword:
            if keyword in news["description"]:
                isCorrect = True
                break
        if not isCorrect:
            continue

        newNews = {
            'newsLink': news["link"],
            'newsTitle': news["title"],
            'newsDescription': news["description"],
            'newsDate': str(date)[:10]
        }
        #### 새로운 뉴스를 더하자
        print(newNews)
    if params['start'] >= min(200, total):
        break
    params['start'] += params['display']

