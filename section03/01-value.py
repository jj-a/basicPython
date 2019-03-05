# section03 / 01-value.py
# 변수를 정의하는 파이썬만의 다양한 방법


# 튜플을 통한 변수 생성
a, b = ("python", "bigdata")
print(a, b)

(a, b) = "hello", "world"
print(a, b)

# 리스트를 활용한 변수 생성
a, b = ["python", "bigdata"]
print(a, b)

[a, b] = "hello", "world"
print(a, b)

[a, b] = ["안녕", "파이썬"]
print(a, b)

# 동일한 값을 갖는 여러 변수 생성
a = b = c = 123
print(a, b, c)

# swap 기능
x = 3
y = 5
x, y = y, x
print(x, y)
