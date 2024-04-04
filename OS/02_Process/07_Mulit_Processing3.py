## Multi Processing3
## 다른 작업을 각자 다른 프로세스에

from multiprocessing import Process
import os
import time

def Sungchan():

    time.sleep(1)

    print('Sungchan Process ID is ', os.getpid())
    print('Parent Process ID is ', os.getppid())
    print()


def Taro():

    time.sleep(1)

    print('Taro Process ID is ', os.getpid())
    print('Parent Process ID is ', os.getppid())
    print()


def Anthon():
    
    time.sleep(1)

    print('Anthon Process ID is ', os.getpid())
    print('Parent Process ID is ', os.getppid())
    print()



if __name__ == '__main__':
    print('07.py Process ID is... ', os.getpid())
    child1 = Process(target=Sungchan)
    child1.start()


    child2 = Process(target=Taro)
    child2.start()


    child3 = Process(target=Anthon)
    child3.start()
