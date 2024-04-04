import threading
import os
import time

# 무한 루프
def something(word):
    while True:
        print(word)
        time.sleep(3)


# 1 Process 2 Thread(Main, sub)
if __name__ == '__main__': # 메인스레드
    print('Process ID : ', os.getpid())
    # something 함수가 출력할 word 매개변수는 args=에 튜플 형태로 전달
    t = threading.Thread(target=something, args=('RIIZE',)) # 스레드 추가 생성 -> something 함수 작업

    # daemon thread = 메인 프로세스의 기능이 끝나면 함께 종료됨
    # 3초마다 실행되는 something 함수가 Main Thread가 끝나면 함께 끝남
    # 파이썬 프로세스가 생성되면 기본적으로 메인스레드를 갖게됨
    
    t.daemon = True
    t.start()
    print('Iteration is Main Thread')
    while True:
        try:
            print('always...')
            time.sleep(1)
        except KeyboardInterrupt:
            print('TBC')
            break