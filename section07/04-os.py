# section07 / 04-os.py
# OS 내장 모듈
# 운영체제 자체의 기능에 접근할 수 있는 기능을 제공하는 모듈

import sys  # 현재 시스템의 정보를 제공
import os  # 운영체제 기능에 접근

print(sys.platform)

if sys.platform == "win32":
	command = "dir"
else:
	command = "ls -l"

os.system(command)
