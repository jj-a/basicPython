# section09 / 02-line2.py
# pyplot의 옵션 설정

import os
from matplotlib import pyplot
# 데이터 샘플
from sample import newborn
from sample import year

pyplot.figure()

pyplot.title("Newborn Babies of Year")
pyplot.plot(newborn, label="Number of Newborn Babies",
            linestyle="--", marker=".", color="#ffccdd")

pyplot.legend()  # label 속성 적용
pyplot.grid()  # grid 보여주기

pyplot.xlabel("year")
pyplot.ylabel("newborn babies")

# x축 index value 변경
pyplot.xticks([0, 1, 2, 3, 4], year)

pyplot.savefig("section09/line2.png")
pyplot.show()


print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.realpath(__file__))
