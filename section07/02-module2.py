# section07 / 02-module2.py
# 모듈(module)의 활용
# 모듈: 다른 프로그램에서 활용하기 위한 프로그램 조각

import mod2 as mod
from mod2 import Member

member = mod.Member("pypy", "python@hello.py")
member.view_info()

member = Member("java", "java@oracle.com")
member.view_info()

