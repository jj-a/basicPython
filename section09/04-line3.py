# section09 / 04-line3.py
# 다중 선 그래프

from matplotlib import pyplot
import numpy

from sample import seoul
from sample import busan
from sample import daegu
from sample import inchun
from sample import label

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12

pyplot.figure()
pyplot.grid()

pyplot.title("2017년 주요도시 교통사고")
pyplot.xlabel("월")
pyplot.ylabel("교통사고")

# 수치 입력
pyplot.plot(seoul, label="서울")
pyplot.plot(busan, label="부산")
pyplot.plot(daegu, label="대구")
pyplot.plot(inchun, label="인천")

# 범위 설정
pyplot.xlim(0, 11)
pyplot.ylim(0, 4000)

# 범주를 표시하도록 설정
pyplot.legend(title="도시", loc="center left", shadow=True)


# x축의 각 지점에 적용될 라벨 설정
# 0부터 1씩 증가하는 label 리스트 만큼의 크기를 갖는 리스트
x = list(range(0, len(label)))

# x축 
pyplot.xticks(x, label)

pyplot.savefig("section09/line3.png", dpi=200)  # dpi 해상도 설정
pyplot.show()
