# section09 / 09-pie.py
# 원형 그래프
# 전체를 기준으로 한 부분의 상대적 크기를 표시하는 그래프

import numpy
from matplotlib import pyplot
from sample import seoul
from sample import busan
from sample import label

# 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumSquare'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (8, 7)

pyplot.figure()
pyplot.title("스마트폰 점유율")  # 제목

# 표시할 데이터 설정
ratio = [3700, 2800, 1300, 590, 600]  # 라이브러리가 자동으로 비율 계산
labels = ["Apple", "삼성", "LG", "Sony", "기타"]
colors = ["#f4de42", "#3f58d1", "#de4949", "#5ab6e7", "#e9c6ec"]

# 확대 비율
explode = [0.0, 0.0, 0.0, 0.2, 0.1]

# 파이 차트 표시
# 데이터, 라벨, 색상, 확대, 수치값 표시형식, 그림자, 시작각도
# autopct 파라미터 설정 안 할 경우 수치값 표시 안됨
# 의미: %0.2f (소수점 둘째자리까지 표시)
# startangle 기본값= 0도
# 각 데이터 항목들은 반시계 방향으로 회전하면서 배치됨

pyplot.pie(ratio,
           labels=labels, colors=colors, explode=explode,
           autopct="%0.2f%%", shadow=False, startangle=90)

pyplot.legend()

pyplot.savefig("section09/pie.png", dpi=200)
pyplot.show()

pyplot.close()
