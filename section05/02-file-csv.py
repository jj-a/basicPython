# section05 / 02-file-csv.py
# csv 생성/읽기

grade = [{"name": "홍길동", "kor": 90, "eng": 85, "mat": 100},
         {"name": "무궁화", "kor": 30, "eng": 80, "mat": 90},
         {"name": "라일락", "kor": 60, "eng": 55, "mat": 70},
         ]

tpl = "{0}, {1}, {2}, {3}\n"


# csv 파일 저장을 위한 f 객체 생성
# Excel: csv는 euc-kr 형식
# SublimeText 에디터를 쓸 경우 euc-kr은 못읽으니 주의 =..????????
with open("section05/grade.csv", "w", encoding="utf-8") as f:
    f.write("이름 국어 영어 수학\n")
    for item in grade:
        tmp = tpl.format(item["name"], item["kor"], item["eng"], item["mat"])
        f.write(tmp)


with open("section05/grade.csv", "r", encoding="utf-8") as f:
    csv_list = f.readlines()
    print(csv_list)

    print("\n 이름  국어 영어 수학 합계 평균")

    for i, line in enumerate(csv_list):
        if i>0:
            item = line.strip().split(",")
            name = item[0]
            kor = int(item[1])
            eng = int(item[2])
            mat = int(item[3])
            total = kor+eng+mat
            aver = total//3
            tpl = "{0}  {1}  {2}  {3}  {4}  {5}"
            print(tpl.format(name, kor, eng, mat, total, aver))
