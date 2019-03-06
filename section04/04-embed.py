#/section04/04-embed.py
#파이선 내장 함수들

#자료형 조회
a=123
print(type(a))

b=123.45
print(type(b))

print(type("Hello"))
print(type(True))
print(type([1,2]))             #list
print(type((1,2)))             #tuple
print(type({"name":"Python"})) #dict
#----------------------------------------------
#형변환
x="123"
y="45"
print(x+y)

x1=int(x)
y1=int(y)
print(x1+y1)

x2=float(x1)
y2=float(y1)
print(x2+y2)

print(str(x2) + str(y2))
#---------------------------------------------
#수학관련 함수
print(pow(2,3))  # 2*2*2
print(abs(4))    # 절대값
print(abs(-3.5))

# 나눗셈의 연산 결과를 정수 부분의 
# 몫과 나머지로 계산하여 튜플로 리턴
print(divmod(7, 3)) # (2,1)

hours = 800
k = divmod(800, 24)
tpl = "{0}일 {1}시간"
print(tpl.format(k[0], k[1]))

days, hours = divmod(960, 24)
print(tpl.format(days, hours))
#---------------------------------------------
#연속성 자료형과 관련된 내장 함수
#리스트, 튜플, 딕셔너리

a={1, 2, 3}
print(len(a))

a=[1, 2, 3]
print(max(a))
print(min(a))
print(sum(a))

print(sum(a)/len(a)) #평균
#---------------------------------------------
a = "Python"
b = list(a)  #['P', 'y', 't', 'h', 'o', 'n']
print(b)     
b = tuple(a) #('P', 'y', 't', 'h', 'o', 'n')
print(b)

c = (1, 2, 3)
d = list(c)
print(d)
d = tuple(c)
print(d)

e = [10, 20, 30]
f = list(e)
print(f)
f = tuple(e)
print(f)
#---------------------------------------------
#딕셔너리경우 key, value를 별도로 추려내기
g = {"a":100, "b":200}
h = list(g.keys())
print(h)

i = list(g.values())
print(i)
i = tuple(g.values())
print(i)
#---------------------------------------------

k = range(1, 10)
print(k)
print(type(k))

mylist = list(k)
print(mylist)       #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(mylist))

k = list(range(1, 10, 3))
print(k)            #[1, 4, 7]
#-----------------------------------------
#리스트 자체를 정렬하기
data = [1, 4, 5, 3, 2]
#print(data.sort()) #원본 리스트 자체가 정렬

k = sorted(data)
print(data)        #원본 변화 없음
print(k)



