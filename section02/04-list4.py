# section02 / 04-list4.py
# 리스트 조작하기


# 리스트 사칙연산
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2    # 리스트가 합쳐짐
print(list3)

list4 = list1 * 3    # 리스트가 해당 횟수만큼 반복되어 저장
print(list4)


# 리스트 수정, 확장, 축소
mylist = [1, 2, 3]

mylist[2] = 4
print(mylist)

mylist[1:3] = [20, 30]
print(mylist)

# 주어진 범위보다 작은 갯수를 갖는 리스트 지정 -> 리스트 잘림
mylist[1:3] = [1000]
print(mylist)

# 주어진 범위보다 많은 갯수를 갖는 리스트 지정 -> 리스트 확장
mylist = [1, 2, 3]
mylist[1:2] = [7, 8, 9, 0]  #[1, 7, 8, 9, 0, 3]
print(mylist)
print("-" * 30)

# del() : 리스트 원소 삭제
mylist = [1, 2, 3, 4, 5]
del(mylist[1])
print(mylist)

mylist = [1, 2, 3, 4, 5]
del(mylist[1:3])
print(mylist)

mylist = [1, 2, 3, 4, 5]
mylist[1:3] = []    # del()과 동일
print(mylist)


# 리스트의 원소 삼입과 확장 비교
mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist[1] = [100, 200]
print(mylist)
print(len(mylist))

# 슬라이싱으로 접근하는 경우 주어진 범위를 [확장]하는 개념
mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist[1:2] = [100, 200]
print(mylist)
print(len(mylist))