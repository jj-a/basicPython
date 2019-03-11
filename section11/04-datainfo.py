# section11 / 04-datainfo.py
# 기초통계 산출하기

from pandas import DataFrame
from sample import grade_dic

df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])

print(df)

print(df.head())  # 파라미터 없을 경우 기본 5줄
print(df.head(2))  # 전체에 대한 처음 2줄만 추출
print(df["영어"].head(2))  # 특정 열에 대한 첫 2줄

print(df.tail(2))  # 마지막 2줄만 보기
print(df["영어"].tail(2))  # 특정 열에 대한 마지막 2줄

# 요약정보의 개별 조회 (각 열 혹은 특정 열에 대해 n/a를 제외한 값의 수 반환)
print(df.count())
print(df["영어"].count())

print(df.min())
print(df["영어"].min())

print(df.max())
print(df["영어"].max())

print(df.mean())  # 평균
print(df["영어"].mean())

print(df.std())  # 표준편차
print(df["영어"].std())

print(df.median())  # 중앙값 (2사분위수)
print(df["영어"].median())

print(df.quantile(q=0.5))  # 사분위수(중앙값: 50% 위치의 값)
print(df["영어"].quantile(q=0.5))

print(df.quantile(q=0.25))  # 1사분위수(25% 위치의 값)