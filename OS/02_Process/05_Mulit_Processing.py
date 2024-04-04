## Multi Processing

# 자식 객체를 생성하는 클래스
from multiprocessing import Process
import os

# 함수를 하위 프로세스를 만들어 맡긴다
# 05.py 프로그램은 해당 하위 프로세스의 부모 프로세스가 됨
def func():
    print('...Half-assed function...')
    print('My Process ID is', os.getpid()) # 하위 프로세스 ID
    print('Parents Process Id is', os.getppid()) # 05.py ID

if __name__ == '__main__':
    print('05.py Process ID is ', os.getpid())
    # target 매개변수는 프로세스에 시킬 작업을 정의
    child = Process(target=func).start()