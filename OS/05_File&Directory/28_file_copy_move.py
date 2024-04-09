# 파일의 복사, 이동
import os
import shutil

pwd = '/Users/yeonsu/Desktop/OZ_BE/OS/05_File&Directory'
filenames = os.listdir(pwd)

for filename in filenames:
    if 'siren' in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        #shutil.copy(origin, os.path.join(pwd, 'siren_copy.txt'))
        shutil.move(origin, os.path.join(pwd, 'Empty_dic') )