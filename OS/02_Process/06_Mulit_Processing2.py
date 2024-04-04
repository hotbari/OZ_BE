## Multi Processing2
## 동일한 작업을 각자 다른 프로세스에

from multiprocessing import Process
import os
import time

def func():
    print('...Half-assed function...')
    print('My Process ID is', os.getpid()) # 하위 프로세스 ID
    print('Parents Process Id is', os.getppid()) # 06.py ID

if __name__ == '__main__':
    print('06.py Process ID is ', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(1)

    child2 = Process(target=func)
    child2.start()
    time.sleep(1)

    child3 = Process(target=func)
    child3.start()
    time.sleep(1)

    child4 = Process(target=func)
    child4.start()