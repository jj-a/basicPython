# section11 / 05-boxplot.py
# 상자그림
# 데이터에 이상이 있는지, 어느정도 분포되어 있는지 알 수 있음

from matplotlib import pyplot
from pandas import DataFrame
from sample import grade_dic

df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 7)

# 국어 점수에 대한 상자그림 보기
pyplot.figure()
pyplot.grid()  # 격자선 표시
df.boxplot("국어")

pyplot.savefig("section11/boxplot1.png", dpi=300)  # dpi 해상도 설정
pyplot.show()

pyplot.close()