# section10 / 03-wordcloud_korean.py
# 배경 이미지 모양으로 Wordcloud 출력

from matplotlib import pyplot
import numpy
from wordcloud import WordCloud
from wordcloud import STOPWORDS  # 금지어 설정
from PIL import Image  # 이미지 처리 모듈 (내장모듈)

from collections import Counter  # 빈도수 계산 (파이썬 기본)
from konlpy.tag import Okt  # 한글 형태소 분석기


text = ""
with open("section10/res/대한민국헌법.txt", "r", encoding="utf-8") as f:
    text = f.read()


# text 변수가 가지고 있는 내용을 기반으로 형태소 분석
# 형태소 분석 클래스 객체 생성
nlp = Okt()
# 명사들만 추출 -> 리스트 형식으로 반환
nouns = nlp.nouns(text)
# print(nouns)

# 명사 형태의 단어들로 리스트를 만들고 한글자로 된 단어는 잘라냄 (개개인 판단)
words = []

for n in nouns:
    if(len(n)) > 1:
        words.append(n)

# 빈도수 계산
# Counter 객체를 통해 리스트 원소들의 빈도수를 계산하여 딕셔너리 값으로 반환
count = Counter(words)
# print(count)

# 가장 많이 등장한 상위 100개 추출
most = count.most_common(100)
print(most)

# wordCloud 객체가 요구하는 형식으로 딕셔너리를 직접 구성
tags = {}

for n, c in most:
    tags[n] = c
print(tags)

#  수집 결과를 활용하여 워드클라우드 생성
# 한글 워드클라우드를 작성하는 경우 글꼴 이름 확인할 것


# 금지어 설정 / STOPWORDS.add()
ignore = set(STOPWORDS)
# 제외단어 리스트
except_words = []
for i in except_words:
    ignore.add(i)
# print(ignore)

# 꾸밈기능: 배경 이미지 위에 출력
img = Image.open("section10/res/book.png")

img_array = numpy.array(img)

# WordCloud 클래스의 객체 생성
# width, height = 모니터 해상도 크기
#  scale = 보고서용 3.0, 인쇄용으로는 2~3배 크게
wordcloud = WordCloud(width=1200, height=800, scale=3.0, stopwords=ignore,
                      font_path="NanumGothic", max_font_size=150, max_words=100,
                      mask=img_array, background_color="#551e3f"  # 배경이미지 관련 옵션
                      )   

# 단어 빈도수 계산
# WordCloud 객체를 사용하여 텍스트에 대한 단어 빈도수 추출
# 딕셔너리를 직접 정의해도 무관
gen = wordcloud.generate_from_frequencies(tags)
# gen = wordcloud.generate(text)
print(gen.words_)

pyplot.figure()  # 그래픽 생성

# 그래픽 표시  데이터를 단어 빈도수에 대한 딕셔너리로 지정
# interpolation: 워드클라우드에 등록되어있는 정렬방식
pyplot.imshow(gen, interpolation="bilinear")
wordcloud.to_file("section10/simple4.png")  # 크기는 scale에서 조정가능

pyplot.close()
