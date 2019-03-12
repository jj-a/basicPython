# section11 / 12-refine3.py
# 데이터 정제 3 - 이상치 정제

# 결측치 (Missing Value) : 누락된 값, 비어있는 값
# 이상치 (Outlier) : 정상 범주에서 크게 벗어난 값

from pandas import DataFrame
from sklearn.impute import SimpleImputer  # sklearn 모듈
from sample import grade_dic
from print_df import print_df
import numpy


df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])
print_df(df)

# 국어점수에 대한 이상치 필터링
r = df.query("국어 > 100")
print_df(r)

# 필터링 된 이상치 데이터에 대한 인덱스 추출
r_index = list(r.index)
print_df(r_index)

# 이상치를 갖는 인덱스에 대한 국어점수를 결측치로 변경
for i in r_index:
	df.loc[i, "국어"] = numpy.nan

print_df(df)


# 결측치를 정제할 규칙 정의
imr = SimpleImputer(missing_values = numpy.nan, strategy="mean")

# dataframe의 값에 대해 규칙 적용
df_imr = imr.fit_transform(df.values)
print_df(df_imr)

# 적용된 규칙으로 새로운 데이터 프레임 생성
re_df2 = DataFrame(df_imr, index=df.index, columns=df.columns)
print_df(re_df2)
