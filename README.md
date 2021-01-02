# Youtube Unboxing : 유튜버 분석 서비스
1. [시연 영상](#시연-영상)
1. [기술 스택](#기술-스택)
1. [기획 의도](#기획-의도)
1. [개발 일정](#개발-일정-및-팀원-구성)
1. [맡은 역할](#맡은-역할)
1. [각 페이지 소개](#각-페이지-소개)

# 시연 영상

<h2>완벽한 분석 기능</h2>
<img src="README_img/detail.gif" width=80% />
<!-- ![비디오](img/detail.gif) -->
<h4 style="margin-bottom: 10%">
    구독자 수, 조회수 같은 기본적인 정보부터
    <br />커뮤니티, 뉴스 분석까지
    <br />한 화면에서 모두 만나보세요.
</h4>
<hr width="80%">
<h2>간편한 검색 기능</h2>
<img src="README_img/search.gif" width=80% />
<h4 style="margin-bottom: 10%">
    원하는 유튜버를 검색해 볼 수 있습니다.
    <br />만약 내가 찾는 유튜버가 없다면?
    <br />자유롭게 추가하세요.
</h4>
<hr width="80%">
<h2>손쉬운 비교하기 기능</h2>
<img src="README_img/compare.gif" width=80% />
<h4 style="margin-bottom: 10%">
     번거롭게 하나하나 비교할 필요 없이
    <br />한 화면에서 손쉽게 두 유튜버를
    <br />비교해 보세요.
</h4>
<hr width="80%">
<h2>강력한 유튜버 추천 기능</h2>
<img src="README_img/user.gif" width=80% />
<h4 style="margin-bottom: 10%">
    나와 관심항목이 같은 사람들이
    <br />즐겨찾는 유튜버를 추천해 드립니다
    <br />바로 확인해 보세요.
</h4>
<hr style="margin-bottom: 15%;">

# 기술 스택

<img src="README_img/technology-stack.png" width="70%" style="margin-top: 3%; margin-bottom: 7%">
<hr width="70%" />
<img src="README_img/system-architecture.png" width="70%" style="margin-top: 3%;"><br>

- `FrontEnd`는 `Vue`를 이용해 구현했고, `Vuetify`를 이용해 UI를 디자인했습니다.

- `BaekEnd`는 `Spring`과 `Django` 2개의 서버를 두었습니다.
  두 서버는 서로 다른 역할을 수행합니다.

- `Spring 서버`는 `REST API`를 이용해 사용자로부터 온 요청에 응답하여
  DB에서 필요한 정보를 조회해 Front단에서 요청한 정보를 보냅니다.

- `Django 서버`는 유튜버 데이터에 관한 업무를 담당합니다.
  저희 DB에 없는 유튜버를 사용자가 추가할 경우, 장고 서버가 해당 유튜버의 정보를 수집합니다.
  또한, 수집된 정보들을 주기적으로 업데이트하는 역할도 수행합니다. 관련 데이터는 `Naver, Daum, Youtube API`를 통해 가져옵니다.

- 데이터베이스는 `mariaDB`를 사용했고, 로그인은 `Kakao 로그인`을 사용했습니다.
<hr />

# 기획 의도

<img src="README_img/introduce1.png" width="70%" style="margin-top: 3%;">
<hr width="70%"/>
<img src="README_img/introduce2.png" width="70%" style="margin-top: 3%;">
<hr width="70%" />
<img src="README_img/introduce3.png" width="70%" style="margin-top: 3%;">
<hr width="70%" />
<img src="README_img/introduce4.png" width="70%">

<hr />

# 개발 일정 및 팀원 구성

<img src="README_img/schedule.png" width="70%"><br>

<hr width="80%">

<img src="README_img/team.png" width="70%">

<!-- :sunglasses: 김주희

:cat: 김태민

:smirk: 박진홍

:cloud: 이상민

:zzz: 홍기환 -->

<hr />

# 각 페이지 소개

<img src="README_img/detail1.png" width="80%"><br>

<img src="README_img/detail2.png" width="80%"><br>

<img src="README_img/detail3.png" width="80%"><br>

<img src="README_img/detail4.png" width="80%"><br>

<img src="README_img/detail5.png" width="80%"><br>

<img src="README_img/detail7.png" width="80%"><br>

<img src="README_img/detail8.png" width="80%"><br>

<img src="README_img/detail9.png" width="80%"><br>

<img src="README_img/detail10.png" width="80%"><br>

<img src="README_img/detail11.png" width="80%"><br>

<img src="README_img/detail12.png" width="80%"><br>

<img src="README_img/detail13.png" width="80%"><br>

<img src="README_img/detail14.png" width="80%"><br>

<img src="README_img/detail15.png" width="80%"><br>

<hr />

<!--
# Git branch 현황

img src="README_img/gitFlow.jpg" width="70%"
br

- `master` : 프로젝트의 최종 결과물 및 관련 문서들을 정리하였습니다.
- `develop` : 현재 개발 단계에 있어 master로 merge하기 전에 검토하는 브렌치입니다.
- `frontDev` : Vue의 개발 진행을 총괄하는 브렌치입니다. 세부 기능별 개발 브렌치를 가지고 있습니다.
- `backDev` : Spring의 개발 진행을 총괄하는 브렌치입니다. 세부 기능별 개발 브렌치를 가지고 있습니다.
- `dataDev` : django 서버 및 데이터 수집을 총괄하는 브렌치입니다. 세부 기능별 개발 브렌치를 가지고 있습니다.
div style="margin-bottom: 15%;"/

-->

