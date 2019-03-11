# section11 / 01-series.py
# 

# pandas 패키지
from pandas import Series

# 리스트, 인덱스 추상적
items = [10, 30, 50, 70, 90]
print(items)

# 시리즈, 인덱스가 열로 추가
column = Series(items)
print(column)

print(column[0])
print(column[1])
print(column[2])

print(column.values)
print(column.index)

# 시리즈 값들을 list로 변환
print(list(column.values))
print(list(column.index))

# 특정 조건에 맞는 항목들만 추출 - 이름[조건식]
in1 = column[column>30]
print(in1)

in2 = column[column<70][column>10]
print(in2)
