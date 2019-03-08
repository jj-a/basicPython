# section09 / 08-box4.py
# 다중 가로 막대 그래프

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

y = numpy.arange(len(label))
print(y)

# 기준축(y)의 좌표와 굵기를 설정한 막대그래프
pyplot.barh(y-0.1, seoul, label="서울", height=0.4, color="#fbed6c")
pyplot.barh(y+0.1, busan, label="부산", height=0.4, color="#7bdddf")

pyplot.legend()

pyplot.xlabel("교통사고 수")  # 데이터(x) 라벨
pyplot.ylabel("월")  # 기준축(y) 라벨
pyplot.yticks(y, label)
pyplot.xlim(0, 4000)  # 데이터(x) 범위

pyplot.savefig("section09/box4.png", dpi=200)  # dpi 해상도 설정
pyplot.show()

pyplot.close()
