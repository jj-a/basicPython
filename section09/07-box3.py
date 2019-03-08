# section09 / 07-box3.py
# 가로 막대 그래프

from matplotlib import pyplot
from sample import newborn
from sample import year

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 7)

pyplot.figure()
pyplot.grid()  # 격자선 표시
pyplot.title("년도별 신생아수")  # 제목

# barh() : 가로 막대그래프 표시
pyplot.barh(year, newborn, label="신생아 수", color="#c1f46c")
pyplot.legend()

pyplot.xlabel("신생아 수")  # 데이터(x) 라벨
pyplot.ylabel("년도")  # 기준축(y) 라벨
pyplot.xlim(350000, 450000)  # 데이터(x) 범위

pyplot.savefig("section09/box3.png", dpi=200)  # dpi 해상도 설정
pyplot.show()

pyplot.close()
