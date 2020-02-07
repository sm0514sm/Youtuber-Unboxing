import json
import requests
from pprint import pprint
from decouple import config
import datetime
# ++ 날짜 형식은 YYYY-MM-DD 형식으로 바꾸기

# YOUTUBER = '피지컬갤러리'

# PATH = '{}.json'.format(YOUTUBER)
# try:
#     with open("{}".format(PATH), 'r', encoding='utf-8-sig') as file:
#         DATA = json.load(file)
# except FileNotFoundError:
#     DATA = dict()


# NEWS_URL = 'https://openapi.naver.com/v1/search/news.json?'
# DISPLAY = 100    # 검색결과 출력 건수(10 ~ 100)
# START = 112      # 검색 시작 위치(1 ~ 1000)

# URL = NEWS_URL

# params = {  # 매개변수
#     'query': YOUTUBER,
#     'display': DISPLAY,
#     'start': START,
#     'sort': 'date'
# }

# headers = {  # 헤더 정보
#     'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
#     'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
# }

# # 요청 결과
# response = requests.get(URL, params=params, headers=headers).text # type str
# result = json.loads(response)   # type dict



# ### 여기에 필터를 추가할 것

# # DATA와 result를 합친다.
# for key, value in result.items():
#     # 기사 목록은 이전 정보들과 합친다.
#     if key == 'items':
#         try:
#             DATA[key] += value
#         except KeyError:
#             DATA[key] = value
#     # 과거 정보는 새로운 정보로 업데이트
#     else:
#         DATA[key] = value


# # 가져온 정보를 json 파일로 만들기
# with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
#     json.dump(DATA, file, indent="\t", ensure_ascii=False)
















# # json으로 저장한 파일을 콘솔창에 print하기
# with open("{}".format(PATH), 'r', encoding='utf-8-sig') as file:
#     json_data = json.load(file)
# pprint(json_data)
# 기본, 게임, 엔터테인먼트, 뷰티, 스포츠, 먹망, 키즈, 동물, 일상, IT
NECESSARY_WORD = [
    ['유튜브', '유튜버', '유투버', '채널'],
    ['게임', 'game'],
    ['엔터테인먼트', '예능', 'entertainment'],
    ['뷰티', '화장', '패션'],
    ['운동', 'Sports', '스포츠', '헬스'],
    ['먹방', '음식', '푸드', 'Food'],
    ['키즈', '어린이', 'Kids'],
    ['동물', '애니멀', 'Animal'],
    ['일상', '브이로그', 'V-log', 'Vlog'],
    ['IT', 'SW', '소프트웨어', '기술', '신제품', '노트북', '컴퓨터', '시스템', '스마트폰', '무선']
]

def get_news_list(youtuber, category, last_updated_date):


    MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    YOUTUBER = '가로세로연구소'  # DB 에서 yno 에 해당하는 channelName or youtubeName 을 입력
    CATEGORY = [8]

    URL = 'https://openapi.naver.com/v1/search/news.json?'
    params = {
        'query': YOUTUBER,
        'display': 100,
        'start': 1,
        'sort': 'date'
    }

    headers = {
        'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
        'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
    }

    category_keyword = NECESSARY_WORD[0]
    for num in CATEGORY:
        category_keyword += NECESSARY_WORD[num]

    # 만약 last updatedDate 가 2019-03-15 면 3월 15일 이후의 기사만 가져와야함
    news_list = []
    while True:
        response = requests.get(URL, params=params, headers=headers)
        response.encoding = 'utf-8'
        response = response.text
        try:
            total = json.loads(response)["total"]
            newses = json.loads(response)["items"]
        except:
            print(json.loads(response))
        for news in newses:
            is_correct = False
            date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(
                news["pubDate"][8:11]), int(news["pubDate"][5:7]))

            # 업데이트되어있는 기사는 추가하지 않음
            if (date - last_updated_date).days < 0:
                break

            # Description 에 특정 키워드가 없는 기사는 추가하지 않음
            for keyword in category_keyword:
                if keyword in news["description"]:
                    is_correct = True
                    break
            if not is_correct:
                continue

            new_news = {
                'newsLink': news["link"],
                'newsTitle': news["title"],
                'newsDescription': news["description"],
                'newsDate': str(date)[:10]
            }
            news_list.append(new_news)
        if params['start'] >= min(1000, total):
            break
        params['start'] += params['display']
    return news_list