# section01 / 06-string_function.py
# 문자열 관련 함수

str = "Life is too short. You need Python"

# len() : 문자열 길이
print(len(str))

print()

# count() : 문자열 개수
print(str.count("i"))
print(str.count("a"))
print(str.count("short"))
print(str.count("nice"))

print()

# rfind() : 문자열의 첫 index값을 오른쪽에서 0부터 카운트하여 반환 (없을 경우 -1)
print(str.rfind("i"))
print(str.rfind("a"))
print(str.rfind("short"))
print(str.rfind("nice"))

print()

# index() : 문자열의 첫 index를 반환 (없을 경우 error)
print(str.index("short"))
# print(str.index("nice"))    # error

print()

# 해당 문자열로 시작하는지 여부 확인
print(str.startswith("L"))
print(str.startswith("l"))
print(str.startswith("Life"))
print(str.startswith("H"))
print(str.startswith("Hello"))

print(str.endswith("N"))
print(str.endswith("n"))
print(str.endswith("Python"))
print(str.endswith("python"))