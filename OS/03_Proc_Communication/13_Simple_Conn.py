from multiprocessing import Process
import os
import time

def writer():
    print(f'{os.getpid()} WRITE FILE')
    with open('13.txt','w') as f :
        f.write('HELLO ~~')

def reader():
    print(f'{os.getpid()} READ FILE')
    with open('13.txt','r') as f :
        print(f.read())

if __name__ == '__main__':
    # 쓰여진 데이터가 있어야 읽을 수 있다
    # 동기 문제를 고려해 writer 우선 작성
    p1 = Process(target=writer)
    p1.start()

    time.sleep(1) # 딜레이로 쓰는 작업 도중 읽는 동작을 방지

    p1 = Process(target=reader)
    p1.start()

    p1.join() # 동작이 끝날 때까지 기다림


