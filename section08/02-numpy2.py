# section08 / 02-numpy2.py
# numpy 모듈


import numpy

# 0부터 15 전까지 순차적으로 증가하는 값들을 원소로 갖는 배열
a = numpy.arange(15)
print(a)

# 100부터 115 전까지 순차적으로 증가하는 값들을 원소로 갖는 배열
b = numpy.array(numpy.arange(100, 115))
print(b)
print(len(b))

# 모든 원소가 실수형 0인 1행3열 배열 생성
c = numpy.zeros([3])
print(c)

# 모든 원소가 정수형 1인 1행 4열 배열
# dtype 기본값 = 'float'
d = numpy.zeros([4], dtype='int')
print(d)

# 모든 원소가 실수형 1인 1행 3열 배열
e = numpy.ones([3])
print(e)

# 모든 원소가 정수형 1인 1행 4열 배열
f = numpy. ones([4], dtype='int')
print(f)

# 모든 원소가 정수형 7인 1행 5열 배열
g = numpy.full([5], 7)
print(g)

# 모든 원소가 실수형 7인 1행 4열 배열
# dtype 기본값 = 'int'
h = numpy.full([4], 7, dtype='float')
print(h)
