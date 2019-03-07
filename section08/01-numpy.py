# section08 / 01-numpy.py
# numpy 모듈


import numpy

arr = [1, 2, 3]
print(arr)

# 리스트를 통한 1차원 배열 만들기
a = numpy.array(arr)
print(a)
print(len(a))

arr2 = [1.2, 3, '4']
print(arr2)

# 실수가 범위가 더 크므로 모든 원소가 실수형으로 변환
b = numpy.array([1, 2.3, 4, 5.6])
print(b)

# 모든 타입이 문자열로 변환
c = numpy.array([1.2, 3, '4'])
print(c)

# 모든 원소의 타입을 int로 지정
d = numpy.array([1, 2.4, 3, 4.6], dtype='int')
print(d)

# 리스트 값을 배열 형태로 변환
arr3 = numpy.array([1, 3, 5, 7, 9])
size = len(arr3)
print("배열의 원소는 %d개입니다." % size)

# 배열 원소 접근
print(arr3[0])
print(arr3[3])

for i in range(0, size):
    print("%d번째 원소: %s" % (i, arr3[i]))