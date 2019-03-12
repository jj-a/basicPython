# section12 / 04-use_module.py
# 크롤러 모듈 사용하기


from Crawler import crawler  # Crawler.py 파일
from sample import naver_news_url  # 가져올 뉴스의 url

# 가져올 페이지의 url과 추출할 영역의 css 셀렉터 지정
html = crawler.select(naver_news_url, encoding="euc-kr", selector="#articleBodyContents")


# 불필요한 태그 제거
for item in html:
	crawler.remove(item, "script")
	crawler.remove(item, "a")
	crawler.remove(item, "br")
	crawler.remove(item, "span")

# 크롤링 결과
print(item.text.strip())
