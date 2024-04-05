from multiprocessing import Pipe, Process
import os

def send(conn):
    print(f'{os.getpid()} SEND DATA TO {os.getppid()}')
    conn.send('Hello, Parents ~')
    conn.close()


# Pipe()는 생성자 함수
if __name__ == '__main__':
    parent, child = Pipe()
    p = Process(target=send, args=(child,)) # sender = child
    p.start()
    print('Process ID : ',os.getpid())
    print(parent.recv()) # Hello, Parents ~ 출력
    p.join() # 프로세스가 작업을 종료할 때까지 기다린다
