# section09 / 01-line1.py
# 그래프

# matplotlib install
from matplotlib import pyplot

# 데이터
data = [10, 11, 12, 13, 14]

# 그래프 설정 시작 -> 모든 그래프 작업 시작시에 호출
pyplot.figure()

# 데이터를 선그래프로 표현
# x축: index / y축: data
pyplot.plot(data)

# 그래프 표시하기
pyplot.show()

# 그래프 관련 설정 해제
pyplot.close()
