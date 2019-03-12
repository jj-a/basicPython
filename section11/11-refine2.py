# section11 / 11-refine2.py
# 데이터 정제 2 - 결측치 대처법

# 결측치 (Missing Value) : 누락된 값, 비어있는 값
# 이상치 (Outlier) : 정상 범주에서 크게 벗어난 값

from pandas import DataFrame
from sample import grade_dic
from print_df import print_df
import numpy

# sklearn 모듈
# Anaconda 환경 기준 scikit-learn 설치 (conda install scikit-learn)
from sklearn.impute import SimpleImputer


df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])
print_df(df)

# 결측치를 특정 값으로 채움 (sklearn 모듈이 아닌 Dataframe 자체 기능)
re_df1 = df.fillna(value=50)
print_df(re_df1)

# scikit-learn 모듈 기반

# 결측치를 정제할 규칙 정의
# 각 열 단위로  평균(strategy="mean") 결측치(missing_values)에 지정
# strategy 옵션 (mean=평균 / median=중앙값 / most_frequent=최빈값(가장많이관측))
imr = SimpleImputer(missing_values = numpy.nan, strategy="mean")

# dataframe의 값에 대해 규칙 적용
df_imr = imr.fit_transform(df.values)
print_df(df_imr)

# 적용된 규칙으로 새로운 데이터 프레임 생성
re_df2 = DataFrame(df_imr, index=df.index, columns=df.columns)
print_df(re_df2)



