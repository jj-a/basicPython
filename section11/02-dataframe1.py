# section11 / 02-dataframe1.py
# 데이터프레임
# 엑셀 / Series의 모음

from pandas import DataFrame
from sample import grade_list
from sample import grade_dic

# 2차원 리스트를 데이터 프레임으로 변환
# df = DataFrame(grade_list)
# print(df)

# 컬럼(열) 이름을 지정하여 새로 생성
c_names = ["국어", "영어", "수학", "과학"]
df = DataFrame(grade_list, columns = c_names)
print(df)
print(df["영어"])

# 인덱스(행) 이름을 지정하여 새로 생성
i_names = ["철수", "영희", "미철", "수현", "호영"]
df = DataFrame(grade_list, index=i_names)
print(df)

# 인덱스와 컬럼 이름 모두 지정
df = DataFrame(grade_list, index=i_names, columns=c_names)
print(df)

# 딕셔너리를 통한 데이터 프레임 만들기
# 딕셔너리의 key는 데이터프레임의 컬럼(열) 이름이 됨
df = DataFrame(grade_dic)
print(df)

# 인덱스 이름을 지정한 데이터 프레임 만들기
# 가장 흔하게 사용하는 문장
df=DataFrame(grade_dic, index=["철수", "영희", "미철", "수현", "호영"])
print(df)