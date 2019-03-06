# section06 / 02-obj2.py


class Member1:
    username = None
    email = None

    # 생성자 함수 앞뒤로 언더바(_) 2개
    def __init__(self):
        print("생성자 함수 호출")
        self.username = "python"
        self.email = "webmaster@soldesk.com"

    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print(tpl.format(self.username, self.email))


mem1 = Member1()
mem1.view_info()


#파라미터를 갖는 생성자

class Member2:
    username = None
    email = None

    # 생성자 함수 앞뒤로 언더바(_) 2개

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print(tpl.format(self.username, self.email))


mem2 = Member2("pypy", "python@hello.py")
mem2.view_info()

mem3 = Member2("jar", "java@hate.you")
mem3.view_info()

