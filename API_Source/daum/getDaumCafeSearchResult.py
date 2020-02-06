 # -*- encoding: utf-8 -*-
from decouple import config
import json
import requests
from pprint import pprint
import datetime


NECESSARY_WORD = [
    ['유튜브', '유튜버', '유투버', '채널', 'youtube', 'youtuber'],  # 0 
    ['게임', 'game'], # 1
    ['엔터테인먼트', '예능', 'entertainment'], # 2
    ['뷰티', '화장', '패션', 'beauty', 'makeup'], # 3
    ['운동', 'Sports', '스포츠', '헬스', 'health', 'fitness', '피트니스'], # 4
    ['먹방', '음식', '푸드', 'Food', '식사'], # 5
    ['키즈', '어린이', 'Kids'], # 6
    ['동물', '애니멀', 'Animal'], # 7
    ['일상', '브이로그', 'V-log', 'Vlog'], # 8
    ['IT', 'SW', '소프트웨어', '기술', 'technology', '신제품', '노트북', '컴퓨터', '시스템', '스마트폰', '무선', '과학'],  # 9
]


def date_is_valid(dateStr): # ex) '2019-03-16'
    global lastUpdate
    article_date = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    if (article_date - lastUpdate).days > 0:
        return True
    else:
        return False


def get_daumCafe_search_result(YOUTUBER):
    global lastUpdate
    # API_KEY를 더 넣도록 합시다.
    API_KEYS = [config('DAUM_API_KEY'), 'temporary_key1', 'temporary_key2', 'temporary_key3']
    
    ######### YOUTUBER를 활용해, searchKeyword, lastUpdate, category 등등을 가져온다.
    youtuber = 5 # 유튜버 객체, 
    searchKeyword = '피지컬갤러리' # 해당 youtuber의 searchKeyword
    lastUpdate = datetime.datetime.strptime('2019-1-1', '%Y-%m-%d') # 가장 최근 업데이트 날짜
    keywords = NECESSARY_WORD[0]
    youtuber_category = [2, 4] # 해당 유튜버 카테고리 가져오자

    for add_category in youtuber_category:
        keywords += NECESSARY_WORD[add_category]

    page = 1
    MORE_PAGES = True
    MORE_DATES = True
    
    DEFAULT_MAX = 6  # 6이면, 6 * 50 인 300개 검색
    MAX_page = DEFAULT_MAX
    
    while MORE_PAGES and MORE_DATES:
        if page >= MAX_page:
            MORE_PAGES = False
        
        params = {
            'query': searchKeyword,
            'sort': 'recency',
            'page': page,
            'size': 50
        }

        URL = 'https://dapi.kakao.com/v2/search/cafe'

        for API_KEY in API_KEYS:
            headers = {
                'Authorization': 'KakaoAK ' + API_KEY
            }
            response = requests.get(URL, headers=headers, params=params)
            response_dict = json.loads(response.text)
            if response.status_code == 200:
                total_count = response_dict.get('meta').get('total_count') # 검색 결과 수
                break
        else:
            # 모든 API_KEY를 다 썼을 경우
            return "---------- Can't get daum cafe articles since api keys are ran out. ----------"

        MAX_page = min(DEFAULT_MAX, total_count // 50)

        documents = response_dict.get('documents')  # 가져온 글들의 모든 목록
        
        if (response.status_code == 200):
            for document in documents:
                contents = document.get('contents')
                if date_is_valid(document.get('datetime')[:10]):
                    for keyword in keywords:
                        if keyword in contents:
                            new_rows = {
                                'yno': youtuber,
                                'articleTitle': document.get('title'),
                                'articleLink': document.get('url'),
                                'articleDescription': document.get('contents'),
                                'articleDate': document.get('datetime')[:10],
                            }
                            # 여기서 바로 저장
                            # DB에 저장
                            # objects.save() 가즈아아아아
                            break
                else:
                    MORE_DATES = False
                    break
        page += 1

if __name__ == '__main__':
    get_daumCafe_search_result('a')