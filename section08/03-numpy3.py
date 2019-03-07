# section08 / 03-numpy3.py
# numpy 배열 연산


import numpy

grade = numpy.array([82, 76, 91, 65])
print("grade", grade)

# 모든 원소에 2 더하기
new1 = grade + 2
print(new1)

# 모든 원소에 2 빼기
new2 = grade - 5
print(new2)

print()

# numpy 배열끼리의 연산
arr1 = numpy.array([10, 15, 20, 25, 30])
arr2 = numpy.array([2, 3, 4, 5, 6])
arr3 = arr1 + arr2

print("arr1", arr1)
print("arr2", arr2)
print("+   ", arr3, "\n")

arr3 = arr1 - arr2

print("arr1", arr1)
print("arr2", arr2)
print("-   ", arr3, "\n")


sample = numpy.array([82, 77, 95, 60])
print("총점: %d" % numpy.sum(sample))
print("평균: %d" % numpy.average(sample))
print("최대값: %d" % numpy.max(sample))
print("최소값: %d" % numpy.min(sample))



