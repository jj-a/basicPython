# section11 / 13-graph.py
# 데이터프레임 시각화

# 결측치 (Missing Value) : 누락된 값, 비어있는 값
# 이상치 (Outlier) : 정상 범주에서 크게 벗어난 값

from matplotlib import pyplot
from pandas import DataFrame
from sklearn.impute import SimpleImputer  # sklearn 모듈
from print_df import print_df
import numpy

from sample import traffic

df = DataFrame(traffic)
print_df(df)


# 데이터 전처리
month = list(df["month"])
# 월에 대한 컬럼만 리스트로 추출
new_name = {}
print_df(month)

# "월" 리스트
for i, v in enumerate(month):
	# 딕셔너리에 {index:value} 형식으로 채워넣음
	new_name[i] = v

# 데이터프레임의 인덱스 변경
df.rename(index=new_name, inplace=True)

# 기존의 "월" 컬럼 삭제
df.drop("month", axis=1, inplace=True)
print_df(df)


# 다양한 그래프 시작화

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 7)


# 상자그림
pyplot.title("2017년 교통사고 변화")
pyplot.grid()

df.boxplot()

pyplot.ylabel("교통사고 수")

pyplot.savefig("section11/boxplot3.png", dpi=200)
pyplot.show()
pyplot.close()


# 선그래프
x = numpy.arange(len(month))

pyplot.title("2017년 월별 교통사고 변화")
pyplot.grid()
pyplot.legend()

df.plot()

pyplot.ylabel("교통사고 수")
pyplot.xticks(x, month)
pyplot.xlim(0, 11)

pyplot.savefig("section11/plot.png", dpi=200)
pyplot.show()
pyplot.close()

