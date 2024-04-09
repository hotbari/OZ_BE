# os 파일 시스템 관련 함수
import os

pwd = '/Users/yeonsu/Desktop/OZ_BE/OS'

#pwd 위치의 디렉토리 내용을 반환
filename = os.listdir(pwd)
print(filename)

# 디렉토리인지 아닌지 여부
print(os.path.isdir(filename[0])) # T
print(os.path.isdir(pwd+'01_OS')) # F

# 파일인지 아닌지 여부
print(os.path.isdir(pwd)) # T
print(os.path.isfile(filename[1])) # F

# 파일이름과 확장자 분리
filepath = pwd + '/' + filename[0]
print(filepath)
name, ext = os.path.splitext(filepath)
print('name : ',name, 'ext : ', ext)


