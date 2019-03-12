# section11 / 10-refine1.py
# 데이터 정제 1

# 결측치 (Missing Value) : 누락된 값, 비어있는 값
# 이상치 (Outlier) : 정상 범주에서 크게 벗어난 값

from pandas import DataFrame
from sample import grade_dic
from print_df import print_df


df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])
print_df(df)

# 결측치 여부 확인 : isnull(), isna()   # 둘다 동일한 함수

empty = df.isna()
print_df(empty)

# 결측치의 수를 파악하기 위해 각 열별로 합계 도출 (True 카운트)
empty_sum = empty.sum()
print_df(empty_sum)

# 결측치가 있는 모든 "행" 삭제 (원본은 변화x  삭제결과 리턴)
na1 = df.dropna()

print_df(na1)  # 결측치가 삭제된 데이터 프레임 확인
print_df(na1.isna().sum())  # 결측치 값 개수 확인


# 결측치가 있는 모든 "열" 삭제
na2 = df.dropna(axis=1)

print_df(na2)
print_df(na2.isna().sum())


# "행"의 모든 값이 결측치면 해당 행 삭제
na3 = df.dropna(how="all")
print_df(na3)

# "열"의 모든 값이 결측치면 해당 열 삭제
na4 = df.dropna(how="all", axis=1)
print_df(na4)
