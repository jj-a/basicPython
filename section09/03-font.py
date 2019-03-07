# section09 / 03-font.py
# 시스템 폰트 목록

from matplotlib import font_manager

# 시스템 글꼴 폴더(Fonts) 목록 빌드
font_manager._rebuild()

# 시스템 글꼴 목록을 리스트로 가져오기
font_list = font_manager.findSystemFonts()

for file_path in font_list:
    # 폰트 경로로 폰트 속성 객체 가져오기
    fp = font_manager.FontProperties(fname=file_path)
    font_name = fp.get_name()  # 폰트명 조회
    print("%s >> %s" % (file_path, font_name))
