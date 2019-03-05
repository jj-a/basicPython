# section03 / 04-while.py
# 반복문 (while)

x = 1
while x <= 10:
    print("x = %d" % x)
    x += 1

print()

# 7단 출력
y = 1
while y < 10:
    z = 7 * y
    print("7 * %d = %d" % (y, z))
    y += 1

print()

# 1~10까지의 총합
x = 1
sum = 0
while x <= 10:
    sum += x
    print("x = %d, sum = %d" % (x, sum))
    x += 1
