# section02 / 07-dictionary.py
# 딕셔너리
# HashMap 클래스, JSon과 유사
# {"Key":Value} 형태로 구성

dic = {"name": "무궁화", "phone": "1234567", "birth": "0305"}
print(dic)
print(dic["name"])
print(dic["phone"])

dic["name"] = "라일락"
print(dic["name"])

# print(dic["weight"])  # error

dic["height"] = 175
print(dic["height"])

del(dic["birth"])  # 삭제
print(dic)

# 키가 중복될 경우 마지막값만 적용됨
data = {"msg": "HELLO", "msg": "WORLD", "msg": "PYTHON"}  # 경고
print(data)

# key값은 정수형도 가능
rank = {0: "PYTHON", 30: "R", 10: "JAVA"}
print(rank[0])
print(rank[30])
print(rank[10])
