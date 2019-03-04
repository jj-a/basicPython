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

# startswith() : 해당 문자열로 시작하는지 여부
print(str.startswith("L"))
print(str.startswith("l"))
print(str.startswith("Life"))
print(str.startswith("H"))
print(str.startswith("Hello"))

# endswith : 해당 문자열로 끝나는지 여부
print(str.endswith("N"))
print(str.endswith("n"))
print(str.endswith("Python"))
print(str.endswith("python"))

print()

# upper() : 대문자로 변환
upchar = str.upper()
print(upchar)

# lower() : 소문자로 변환
lowchar = str.lower()
print(lowchar)

print(str.swapcase())    # 대소문자 변환
print(str.capitalize())    # 문장의 첫글자를 대문자로
print(str.title())    # 단어별 첫글자를 대문자로
print(str.replace("Life", "My height"))

print()

k = "     py th on  "
# strip() : 공백 제거
# lstrip() 왼쪽 공백 제거 / rstrip() 오른쪽 공백 제거
print("#", k.lstrip(), "#")
print("#", k.rstrip(), "#")
print("#", k.strip(), "#")

print()

a = ","
# join() : 해당 문자열로 결합
b = a.join("python")
print(b)
