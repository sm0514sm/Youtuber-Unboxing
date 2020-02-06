

#   - 파급력 ( 커뮤니티 언급수(그래프), 뉴스언급수, 조회수 ,구독자 대비 조회수)
def get_influence():
    value = 0

    return value

#   - 활동 지수 ( 최근 10개 영상 업로드 주기 )
def get_activity():
    value = 0
    
    return value

#   - 성장세 ( 구독자 증가 추이 대비 증감량을 꺾은선 그래프로 나타냄, 기준은 주별 )
def get_growth():
    value = 0
    
    return value

#   - 기본 데이터 ( 총 조회수, 구독자수 , 댓글수)
def get_basicstat():
    value = 0
    
    return value

#   - 호감도 ( 좋아요 수, 총 영상의 좋아요, 싫어요 비율, 댓글 수 )
def get_charm(video_list):
    good = 0
    bad = 0
    value = 0
    for video in video_list:
        if not video['good'] or video['good'] == None:
            continue
        good += int(video['good'])
        bad += int(video['bad'])
    if good + bad == 0:
        value = 0
    else:
        value = int(good * 100 / (good + bad))
    return value

#   - 등급 
def get_grade():
    grade = ''
    
    return grade