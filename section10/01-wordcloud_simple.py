# section10 / 01-wordcloud_simple.py
# Word Cloud
# 텍스트 마이닝 (Text Mining) : 문자로 된 데이터에서 가치있는 정보를 얻어내는 분석 기법
# 형태소 분석: 문장을 구성하는 어절들이 어떤 품사로 되어 있는지 파악

from matplotlib import pyplot
from wordcloud import WordCloud

text = ""
with open("section10/res/이상한나라의앨리스.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)

# WordCloud 클래스의 객체 생성
# width, height = 모니터 해상도 크기
#  scale = 보고서용 3.0, 인쇄용으로는 2~3배 크게
wordcloud = WordCloud(width=1200, height=800, scale=3.0)

# 단어 빈도수 계산
# WordCloud 객체를 사용하여 텍스트에 대한 단어 빈도수 추출
# 딕셔너리를 직접 정의해도 무관
gen = wordcloud.generate(text)
print(gen.words_)

pyplot.figure() # 그래픽 생성

# 그래픽 표시  데이터를 단어 빈도수에 대한 딕셔너리로 지정
# interpolation: 워드클라우드에 등록되어있는 정렬방식
pyplot.imshow(gen, interpolation="bilinear")
wordcloud.to_file("section10/simple.png")  # 크기는 scale에서 조정가능

pyplot.close()
