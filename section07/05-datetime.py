# section07 / 05-datetime.py
# 내장 모듈

import datetime as DT

now_time = DT.datetime.now()
print(now_time.year)
print(now_time.month)
print(now_time.day)
print(now_time.hour)
print(now_time.minute)
print(now_time.second)

d = now_time.weekday()
print(d)
days = ("월", "화", "수", "목", "금", "토", "일")
print(days[d])

# 출력 포맷
print(now_time.strftime("%y/%m/%d %H:%M:%S"))
