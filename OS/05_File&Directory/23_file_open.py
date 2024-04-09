# 기본적인 파일 입출력 예제
with open('number_one.txt', 'w') as f :
    f.write('one!')

with open('number_two.txt', 'w') as f :
    f.write('two!')

with open('number_three.txt', 'w') as f :
    f.write('three!')

with open('number_four.txt', 'w') as f :
    f.write('four!')


# 공통된 이름을 통해 복수의 파일을 한 번에 처리
import glob

# # txt확장자 파일에 접근
# # recursive=True : 재귀, 디렉토리의 하위-하위-하위에 접근 가능
for filename in glob.glob('*.txt', recursive=True) :
    print(filename)


# 내용을 한 번에 처리
import fileinput

with fileinput.input(glob.glob('*.txt')) as fi :
    for line in fi:
        print(line)

# 파일 이름 매치
import fnmatch
import os


for filename in os.listdir('.') : # 현재 경로에 있는 파일 모두
    # 여섯글자_세글자 매치되는 파일 찾기
    if fnmatch.fnmatch(filename, '??????_*.txt'): 
        print(filename)