# section01 / 06-formatting.py
# 문자열 format

# %d 정수형
# %f 실수형
# %s 문자열형

str1 = "나는 %d원을 갖고 있어요" % 5000
print(str1)

str2 = "%s 날짜는 %d년 %d월 %d일 입니다."
msg1 = str2 % ("정모", 2019, 3, 4)
print(msg1)
msg2 = str2 % ("약속", 2019, 3, 5)
print(msg2)

print("%d원을 입금했습니다." % 12345)
print("%010d원을 입금했습니다." % 12345)
print("%-010d원을 입금했습니다." % 12345)

print("%s에 살고 있습니다." % "서울")
print("%10s에 살고 있습니다." % "한국")
print("%-10s에 살고 있습니다." % "우리집")

money = 12345.6789
print("%f원입니다." % money)
print("%010.3f원입니다." % money)
print("%10.3f원입니다." % money)
print("%-30.3f원입니다." % money)
print("%.3f원입니다." % money)
print("%0.3f원입니다." % money)

# format() : 해당 index 위치에 값 대입하기
msg1 = "I eat {0} apples." 
print(msg1.format("three"))

msg2 = "{0}은 {1}년 {2}월 {3}일 입니다."
print(msg2.format("오늘", 2019, 3, 4))

msg3 = "{name}은 {yy}년 {mm}월 {dd}일 입니다."
print(msg3.format(name="내일", yy=2019, mm=3, dd=5))

msg4 = "{{파이썬}}은 {}다."
print(msg4.format("쉽"))

