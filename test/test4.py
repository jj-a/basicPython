# test4. 파일 경로, 파일명, 확장자 출력

path = "C:\\myphoto\\helloworld.jpg"

filepath = path[:path.rfind("\\")]
filename = path[path.rfind("\\")+1:]
fileformat = path[path.rfind(".")+1:]

print(filepath)
print(filename)
print(fileformat)
