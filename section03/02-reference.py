# section03 / 02-reference.py
# 값에 의한 호출 (Call by Value) : 정수, 실수, 논리값, 문자열
# 객체 참조에 의한 호출 (Call by Object Reference): 리스트, 튜플, 딕셔너리
# Call by Object Reference = Call by Sharing
# Call by Object Reference는 자바의 Call by Reference와 다름 ***

a = 100
b = 200
print(a, b)

# 객체의 참조 (list, dictionary, tuple)
foo = [1, 2, 3]
bar = foo
print(foo, bar)

foo = [4, 5, 6]
print(foo, bar)

bar = [7, 8, 9]
print(foo, bar)

# 참조된 복사본을 변경하면 원본도 함께 변경 (리스트, 딕셔너리) ->?????????

# 리스트 복사 방법 1
bar = [1, 2, 3]
cp1 = [0, 0, 0]
cp1[0] = bar[0]
cp1[1] = bar[1]
cp1[2] = bar[2]
print(bar, cp1)

cp1[2] = 1000
print(bar, cp1)


# 원본에 영향 없이 리스트, 딕셔너리 객체를 복사하고자 하는 경우
# 슬라이싱
cp2 = bar[:]
print(bar, cp2)
cp2[1] = 12345
print(bar, cp2)

# 함수
cp3 = bar.copy()
cp3[0] = 789
print(bar, cp3)  # 원본에 영향없음