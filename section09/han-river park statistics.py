# han-river park statistics.py
# 한강공원 이용객 현황 통계

import numpy
from matplotlib import pyplot
# data load #
from visitortohanriver import cate1 
from visitortohanriver import cate2
from visitortohanriver import cate3
from visitortohanriver import cate4 
from visitortohanriver import cate5
from visitortohanriver import cate6
from visitortohanriver import label_place

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (15, 7)

pyplot.figure()
pyplot.grid()  # 격자선 표시
pyplot.title("2018년 한강공원 이용객 현황 통계")  # 제목

x = numpy.arange(len(label_place))
print(x)

pyplot.bar(x-0.3, cate1, label="일반이용자", width=0.2, color="#fbed6c")
pyplot.bar(x-0.18, cate2, label="운동시설", width=0.2, color="#7bdddf")
pyplot.bar(x-0.05, cate3, label="자전거", width=0.2, color="#97e80f")
pyplot.bar(x+0.05, cate4, label="주요행사 및 마라톤", width=0.2, color="#e87979")
pyplot.bar(x+0.18, cate5, label="특화공원", width=0.2, color="#cdaffa")
pyplot.bar(x+0.3, cate6, label="기타", width=0.2, color="#f7c1ed")

pyplot.legend()

pyplot.xlabel("지역")  # 기준축(x) 라벨
pyplot.ylabel("이용객 수")  # 데이터(y) 라벨
pyplot.xticks(x, label_place)
pyplot.ylim(0, 11000000)  # 데이터(y) 범위

pyplot.savefig("section09/hanriver2018.png", dpi=300)  # dpi 해상도 설정
pyplot.show()

pyplot.close()
