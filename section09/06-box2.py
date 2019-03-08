# section09 / 06-box2.py
# 다중 막대 그래프

import numpy
from matplotlib import pyplot
from sample import seoul
from sample import busan
from sample import label

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 7)

pyplot.figure()
pyplot.grid()  # 격자선 표시
pyplot.title("2017년 서울, 부산 교통사고 현황")  # 제목

x = numpy.arange(len(label))
print(x)

pyplot.bar(x-0.1, seoul, label="서울", width=0.4, color="#fbed6c")
pyplot.bar(x+0.1, busan, label="부산", width=0.4, color="#7bdddf")

pyplot.legend()

pyplot.xlabel("월")  # 기준축(x) 라벨
pyplot.ylabel("교통사고 수")  # 데이터(y) 라벨
pyplot.xticks(x, label)
pyplot.ylim(0, 4000)  # 데이터(y) 범위

pyplot.savefig("section09/box2.png", dpi=200)  # dpi 해상도 설정
pyplot.show()

pyplot.close()
