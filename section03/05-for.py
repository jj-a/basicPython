# section03 / 05-for.py
# 반복문 (for)

# 1~10까지의 총합  / for(i=1; i<11; i++)
for x in range(1, 11):
    print("x = %d" % x)

print()

# 구구단 7단
for y in range(1, 10):
    z = 7*y
    print("7 * %d = %d" % (y, z))

print()

# 값의 변화 단계 조절
for a in range(0, 100, 10):  # 10씩 증가
    print("a = %d" % a)

print()

# 10~0까지 -2씩 감소
for b in range(10, 0, -2):
    print("b = %d" % b)








