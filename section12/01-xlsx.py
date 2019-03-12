# section12 / 01-xlsx.py
# 엑셀 파일을 통한 데이터 수집

# 필요 모듈 : xlrd, openpyxl
from matplotlib import pyplot
from pandas import DataFrame
from pandas import ExcelFile
from print_df import print_df
import datetime as dt

# 엑셀파일 읽기
xls_file = ExcelFile("section12/children_house.xlsx")

# 엑셀의 sheet 이름들 표시
sheet_names = xls_file.sheet_names
print_df(sheet_names)

# 첫번째 sheet를 dataframe으로 변환
df = xls_file.parse(sheet_names[0])
print_df(df)

# 데이터 전처리 - 이름에 대한 열을 리스트로 추출
city_list = list(df["지역"])
print_df(city_list)

# 새로 적용할 인덱스 이름에 대한 딕셔너리 구조 생성
index_dict = {}
for i, v, in enumerate(city_list):
	index_dict[i] = v

print_df(index_dict)

# 원본에서는 이름에 대한 열을 제거하고 인덱스 이름 변경
df.drop("지역", axis=1, inplace=True)
df.rename(index=index_dict, inplace=True)

# 전국에 대한 데이터는 행 삭제
df.drop(["전국(계)"], inplace=True)

print_df(df)

# 생성된 정보를 엑셀로 저장
df.to_excel("section12/전국어린이집.xlsx", sheet_name="어린이집", na_rep="NaN", index=True, index_label="지역", header=["15년", "16년", "17년"])
# sheet_name: 시트이름
# na_rep: 결측치를 표시할 문자열 (default=빈문자열)
# index: False로 지정할 경우  index 저장 안함
# index_label: index에 표시될 제목 (default=빈문자열)
# header: 각 컬럼의 제목으로 사용될 문자열 리스트 (default=데이터프레임 컬럼명)
# encoding: 파일 인코딩 (default=utf-8)

# 데이터 시각화
# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 7)

# 전체 컬럼에 대한 시각화
df.plot.bar()
pyplot.grid()
pyplot.title("2014~2016년 전국 어린이집 분포")
pyplot.legend()
pyplot.ylabel("어린이집 수")

pyplot.savefig("section12/plot1.png", dpi=200)
pyplot.show()
pyplot.close()
