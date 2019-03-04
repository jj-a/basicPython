# section01 / 05-parse.py
# 문자열의 인덱싱 및 슬라이싱

str = "Life is too short. You need Python"
print(str[3])
print(str[-3])
print(str[-1])

print("#"+str[0:3]+"#")
print("#"+str[5:7]+"#")
print("#"+str[19:]+"#")
print("#"+str[:17]+"#")

print("#"+str+"#")
print("#"+str[:]+"#")
print("#"+str[19:-7]+"#")

jumin = "8712301"
birth = jumin[0:6]
gender = jumin[6]
year = jumin[0:2]
month = jumin[2:4]
day = jumin[4:6]

print("주민등록번호7자리:", jumin)
print("생년월일:", birth)
print("성별:", gender)
print("태어난해:", "19", year)
print("태어난월:", month)
print("태어난날:", day)
