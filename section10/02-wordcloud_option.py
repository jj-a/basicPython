# section10 / 02-wordcloud_option.py
# Word Cloud 모듈 옵션

from matplotlib import pyplot
from wordcloud import WordCloud
from wordcloud import STOPWORDS  # 금지어 설정

text = ""
with open("section10/res/이상한나라의앨리스.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)

# 금지어 설정 / STOPWORDS.add()
ignore = set(STOPWORDS)
ignore.add("alice")
ignore.add("said")
print(ignore)

# WordCloud 클래스의 객체 생성
# width, height = 모니터 해상도 크기
#  scale = 보고서용 3.0, 인쇄용으로는 2~3배 크게
wordcloud = WordCloud(width=1200, height=800, scale=3.0, 
stopwords=ignore, max_font_size=150, max_words=100
)

# 단어 빈도수 계산
# WordCloud 객체를 사용하여 텍스트에 대한 단어 빈도수 추출
# 딕셔너리를 직접 정의해도 무관
gen = wordcloud.generate(text)
print(gen.words_)

pyplot.figure() # 그래픽 생성

# 그래픽 표시  데이터를 단어 빈도수에 대한 딕셔너리로 지정
# interpolation: 워드클라우드에 등록되어있는 정렬방식
pyplot.imshow(gen, interpolation="bilinear")
wordcloud.to_file("section10/simple2.png")  # 크기는 scale에서 조정가능

pyplot.close()
