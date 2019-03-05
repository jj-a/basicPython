# section02 / 09-dictionary3.py
# 딕셔너리 관련 함수

dic = {"name": "홍길동", "kor": 10, "eng": 40}

print(dic["name"])
print(dic.get("name"))

# print(dic["addr"])  # error
print(dic.get("addr"))  # none

# get 함수는 전달하는 key가 존재하지 않을 경우 대신 반환될 값을 함께 설정 가능
print(dic.get("addr", "관철동"))

keys = dic.keys()
print(keys)

# key값을 리스트로 변환
key_list = list(keys)
print(key_list)

# value값을 리스트로 변환
value_list = list(dic.values())
print(value_list)

# key와 value를 튜플로 묶어서 리스트 변환
lists = list(dic.items())
print(lists)
