# section03 / 06-for-list.py
# 연속성 데이터 기반의 반복문 처리

test_str = "Python"
for i in test_str:
    print(i)

print()

test_list = ["python", "is", "good"]
for i in test_list:
    print(i)

print()

count = 0
for i in test_list:
    print("%d번째 원소: %s" % (count, i))
    count += 1

print()

size = len(test_list)
for i in range(0, size):
    print("%d번째 원소: %s" % (i, test_list[i]))

print()

for i, value in enumerate(test_list):
    print("%d번째 값: %s" % (i, value))

