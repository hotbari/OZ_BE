# 파일 관련 예외 -> 운영체제와 관련

try:
    f = open('none.txt','r')
    print(f.read())
    f.close()

except FileNotFoundError as e :
    print(e)
    # 첫 번째 인자로 주어진 클래스가, 두 번째 인자로 주어진 클래스의 하위 클래스가 맞는지 확인
    print(issubclass(FileNotFoundError, OSError)) # True
    print(issubclass(ZeroDivisionError, OSError)) # False
