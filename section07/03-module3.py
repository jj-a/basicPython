# section07 / 03-module3.py
# 객체가 정의된 모듈 참조

import mod3
import mod3 as mod
print(mod3.cal.plus(5, 3))
print(mod.cal.minus(5, 3))

# 모듈에 정의된 특정 기능(여기서는 객체)만 참조
from mod3 import cal

print(cal.plus(5, 3))
print(cal.minus(5, 3))

