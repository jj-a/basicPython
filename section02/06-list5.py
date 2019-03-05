# section02 / 05-list5.py
# 리스트 관련 함수


my_list = [1, 2, 3, 4, 5]

# len(List) : 리스트 길이
size = len(my_list)
print(my_list)
print(size)

# append(Index, Value) : 맨 뒤에 삽입
my_list.append(6)
print(my_list)

# insert(Index, Value) : 중간에 삽입
my_list.insert(1, 10)
print(my_list)

# pop() : FILO(First-In Last-Out) / 마지막 요소 꺼내서 리턴 (삭제)
k = my_list.pop()
print(k)

print(my_list.pop())
print(my_list)

# 리스트 확장
addon = [10, 9, 8, 7]
my_list.extend(addon)    # list + list 연산과 동일
print(my_list)

# count(Value) : 해당 값 카운트
c = my_list.count(2)
print(c)

# index(Value) :  해당 값의 인덱스를 앞에서부터 조회
x = my_list.index(10)
print(x)

# remove(Value) : 해당 값 삭제 (앞부터 검색)
my_list.remove(10)
print(my_list)

# reverse() : 현재 리스트 순서 뒤집기
my_list.reverse()
print(my_list)

# sort() : 오름차순 정렬
my_list.sort()
print(my_list)

# reverse >> 내림차순 정렬
my_list.sort(reverse=True)
print(my_list)

text = "Hello,Python,World,Good"
my_list = text.split(",")
print(my_list)


