# section06 / 01-obj1.py

# 클래스 선언


class Member1:
    userid = "python"
    email = "webmaster@soldesk.com"
    phone = "01012345678"


# 객체 선언
mem1 = Member1()
print(mem1.userid)
print(mem1.email)
print(mem1.phone)

# 객체 선언
mem2 = Member1()
print(mem2.userid)
print(mem2.email)
print(mem2.phone)

print()


# 함수를 내장하는 클래스 정의
# 클래스에 포함되는 함수들은 반드시 첫번째 파라미터에 self를 정의해야 함
class Calc:
    def plus(self, x, y):
        return x+y

    def minus(self, x, y):
        return x-y

    def all(self, x, y):
        a = self.plus(x, y)
        b = self.minus(x, y)
        return (a, b)  # 튜플로 묶어서 여러개의 값을 한번에 리턴


cal = Calc()

print(cal.plus(5, 3))
print(cal.minus(5, 3))

a = cal.all(10, 20)
print(a)

p, m = cal.all(100, 200)
print(p, m)

print()


# 변수와 함수를 모두 내장하는 클래스 정의
class Member:
    username = ""
    email = ""
    
    def join(self, username, email):
        self.username = username
        self.email = email
    
    def view_info(self):
        print(self.username)
        print(self.email)
    

mem1 = Member()
mem1.join("python", "webmaster@soldesk.com")
mem1.view_info()

