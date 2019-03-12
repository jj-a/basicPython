# section12 / 03-html_parser.py
# 네이버 뉴스기사 가져오기

# BeautifulSoup4(bs4) 모듈
from bs4 import BeautifulSoup  # 웹페이지 소스코드 분석 모듈
from print_df import print_df
import requests  # 웹페이지 요청 모듈

# 데이터 참조
from sample import naver_news_url  # 가져올 뉴스의 url
from sample import user_agent  # 웹브라우저 버전 정보


# 데이터 수집 - 웹페이지 html 소스 코드 가져오기

# 접속 세션 생성 (Session= cliend와 server간의 연결단위)
session = requests.Session()


# 현재 세션의 referer 페이지(이전 페이지)를 "없음"으로 강제 설정
# referer값이 없으면 웹서버는 브라우저에서 직접 url을 입력한 것으로 간주
session.headers.update({"referer": None, "User-agent": user_agent})

# 특정 웹페이지 접속 (headers 파라미터로 가져올 컨텐츠 형식 미리 지정)
r = session.get(naver_news_url)

# 가져온 html 코드 확인 (웹페이지 인코딩 형식 확인하여 설정)
r.encoding = "euc-kr"
#print_df(r.text)

# 웹페이지 소스코드 html 분석 객체로 생성
soup = BeautifulSoup(r.text, "html.parser")

# css 선택자를 활용하여 가져오기를 원하는 부분 지정
selector = soup.select("#articleBodyContents")
# print_df(selector)

# 데이터 전처리 2 - 추출된 영역 안에서 불필요한 태그 제거
for item in selector:
	for target in item.find_all("script"):
		target.extract()  # 찾아낸 태그 삭제

	for target in item.find_all("a"):
		target.extract()

	for target in item.find_all("br"):
		target.extract()

	for target in item.find_all("span"):
		target.extract()

# print_df(item)  # 삭제된 항목

print("-" * 50)

# 최종 결과값 확인
result_str = item.text.strip()
print(result_str)

