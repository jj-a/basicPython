# section09 / 10-scatter.py
# 산점도 그래프
# 두 변수 간의 영향력을 보여주기 위해 가로축과 세로축에 데이터 포인트를 그리는 그래프
# 두가지 수치에 대한 관계를 추론하기 위한 근거

from matplotlib import pyplot
from sample import tmp  # 온도
from sample import qty  # 아이스크림 판매량

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 7)

pyplot.figure()
pyplot.title("기온과 아이스크림 판매 수량의 관계")  # 제목


# 산점도
pyplot.scatter(tmp, qty, label="판매 수량", color="#ff8cff")
pyplot.legend()
pyplot.grid()

pyplot.xlabel("기온")
pyplot.ylabel("아이스크림 판매 수량")

pyplot.savefig("section09/scatter.png", dpi=200)
pyplot.show()

pyplot.close()
