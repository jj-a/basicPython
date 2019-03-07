# section07 / mod2.py


class Member:
    username = None
    email = None

    # 생성자 함수 앞뒤로 언더바(_) 2개

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print(tpl.format(self.username, self.email))
