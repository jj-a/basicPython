# section12 / 02-simple_http.py
# 웹상의 데이터 가져오기

# requests 모듈 설치
import requests

# 온라인 상의 text파일 url
simple_text_url = "http://itpaper.co.kr/demo/python.txt"


r = requests.get(simple_text_url)

r.encoding = "utf-8"

print(r.text)
