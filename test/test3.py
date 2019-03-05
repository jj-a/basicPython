# test3. 주민등록번호로 생년월일 출력

reg_code = "801023-1000123"
year = reg_code[0:2]
month = reg_code[2:4]
date = reg_code[4:6]

msg = "당신의 생일은 {0}년 {1}월 {2}일 입니다."
print(msg.format(year, month, date))
