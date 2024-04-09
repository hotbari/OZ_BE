# 경로와 확장자 이용해 파일 찾고, 내용 읽기

import os

# 두 개의 인자(경로, 확장자)를 받는 함수
def searchFile(dirname, extension): 
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            searchFile(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension :
                with open(filepath, 'r', encoding='utf-8') as f :
                    print(f.read())


searchFile('/Users/yeonsu/Desktop/OZ_BE/OS', '.js')
