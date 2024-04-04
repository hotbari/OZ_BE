from multiprocessing import Process
import os
import time

# 무한루프
def Sungchan():
    while True:
        try:
            print('Sungchan Process ID is ', os.getpid())
            print('Parent Process ID is ', os.getppid())
            print()
        except KeyboardInterrupt:
            break
        

def Taro():
    while True:
        try:
            print('Taro Process ID is ', os.getpid())
            print('Parent Process ID is ', os.getppid())
            print()
        except KeyboardInterrupt:
            break


def Anthon():
    while True:
        try:
            print('Anthon Process ID is ', os.getpid())
            print('Parent Process ID is ', os.getppid())
            print()
        except KeyboardInterrupt:
            break



if __name__ == '__main__':
    print('07.py Process ID is... ', os.getpid())
    child1 = Process(target=Sungchan)
    child1.start()
    time.sleep(1)

    child2 = Process(target=Taro)
    child2.start()
    time.sleep(1)

    child3 = Process(target=Anthon)
    child3.start()
    time.sleep(1)
