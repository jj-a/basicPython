# section11 / 06-preprocessing1.py
# 데이터 전처리 (Data Preprocessing) : 분석에 적합하게 데이터를 가공하는 작업


from pandas import DataFrame
from sample import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])

print_df(df)

# 컬럼 순서 변경
# 지정된 순서대로 열이 재정렬된 결과가 반환됨
# 원본은 변화없음. 결과가 적용된 복사본이 생성된다
df1 = df.reindex(columns=["국어", "수학", "과학", "영어"])
print_df(df1)

# 지정된 순서대로 행이 재정렬된 결과가 반환됨
# 원본은 변화없음. 결과가 적용된 복사본이 생성된다
df2 = df.reindex(index=["철수", "영희", "민철", "수현", "호영"])
print_df(df2)

# 컬럼, 인덱스 이름 변경
# 기존이름: 새이름 형식의 딕셔너리로 지정
# columns의  index 중 변경을 원하는 하나만 설정 가능
# 원본은 변화없음. 결과가 적용된 복사본이 생성된다
df3 = df.rename(
    columns={"국어": "kor", "수학": "math", "과학": "sinc", "영어": "eng"},
    index={"철수": "cs", "민철": "mc", "호영": "hy", "영희": "yh", "수현": "sh"})
print_df(df3)

# 원본을 수정하고자 하는 경우 inplace 파라미터에 True를 지정
df.rename(
    columns={"국어": "kor", "수학": "math", "과학": "sinc", "영어": "eng"},
	inplace=True)
print_df(df)
