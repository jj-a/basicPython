# section07 / 01-module1.py
# 모듈(module)의 활용
# 모듈: 다른 프로그램에서 활용하기 위한 프로그램 조각

import mod1
import mod1 as mymod
from mod1 import plus as plus

print(mod1.NAME)
print(mymod.plus(5, 3))
print(mymod.minus(5, 3))
print(plus(5, 3))
