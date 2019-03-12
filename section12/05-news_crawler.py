# section12 / 05-news_crawler.py
# 네이버 뉴스 크롤러


from Crawler import crawler  # Crawler.py 파일
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from matplotlib import pyplot
from pandas import ExcelFile
from pandas import DataFrame
from collections import Counter
from konlpy.tag import Okt
from print_df import print_df


# 접속 조건 설정 #

URL = "https://news.naver.com/"
url_list = []  # 뉴스기사 본문 url 리스트


# 수집할 뉴스기사의 url 조사 #

link_list = crawler.select(URL, encoding="euc-kr", selector=".newsnow_tx_inner > a, .newsnow_imgarea > a, .mtype_img > dt > a, .mlist2 > li > a")

for item in link_list:
	print(item)
	print("-" * 30)

for item in link_list:
	print(type(item.attrs))
	# 각 원소(링크)의 attrs중에 href 속성이 있다면 그 속성값을 별도의 리스트에 추가
	if "href" in item.attrs:
		# read.nhn(뉴스 상세페이지 파일명)이 포함되어 있다면 url_list에 추가
		if "read.nhn" in item["href"]:
			url_list.append(item["href"])

# 집계된 주소 확인
for v in url_list:
	print(v)


# 뉴스기사에 접속하여 본문 크롤링 #

print("-" * 30)
print("뉴스기사 크롤링 시작 >> 총 %d개의 기사를 수집합니다." % len(url_list))
print("-" * 30)

news_content = ""  # 기사 본문 저장 변수

# 뉴스 컨텐츠 가져오기
for i, url in enumerate(url_list):
	print("%d번째 뉴스기사 수집중.. > %s" % (i+1, url))
	# 해당 url의 selector에 맞는 데이터 가져오기
	news_html = crawler.select(url, selector="#articleBodyContents", encoding="euc-kr")

	if not news_html:
		print("%d번째 기사 크롤링 실패" % (i+1))
	else:
		print("%d번째 기사 크롤링 성공" % (i+1))

	# 불필요한 태그 제거
	for item in news_html:
		crawler.remove(item, "script")
		crawler.remove(item, "a")
		crawler.remove(item, "br")
		crawler.remove(item, "span", {"class": "end_photo_org"})

		# 공백을 제거한 텍스트만 저장
		news_content += item.text.strip()


# 수집결과를 기반으로 형태소 분석 #

# 형태소 분석 객체를 통해 수집된 뉴스 본문에서 명사만 추출
nlp = Okt()
nouns = nlp.nouns(news_content)

# 명사들에 대한 빈도수 검사
count = Counter(nouns)

# 가장 많이 사용된 단어 100개 추출
most = count.most_common(100)

# 추출 결과 WordCloud 형식으로 재구성
tags = {}
lists = []
for n, c in most:
	if len(n) > 1:
		tags[n] = c
		lists.append([n, c])

df = DataFrame(lists, columns=["단어", "빈도수"])
print_df(df)
# 엑셀로 저장
df.to_excel("section12/helloworld.xlsx", sheet_name="단어빈도수", encoding="utf-8", index=False)


# 수집결과를 활용하여 WordCloud(워드클라우드) 생성 #

# WordCloud 객체 만들기
wordcloud = WordCloud(font_path="NanumGothic", width=1200, height=800, scale=2.0, max_font_size=200, background_color="#ada0de")

gen = wordcloud.generate_from_frequencies(tags)  #TypeError: '<' not supported between instances of 'NoneType' and 'NoneType'
# print(gen.words_)

# WordCloud 이미지 저장
pyplot.figure()
pyplot.imshow(gen, interpolation="bilinear")
pyplot.axis("off")

wordcloud.to_file("section12/news.png")

pyplot.close()

