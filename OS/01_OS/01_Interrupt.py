# 인터럽트 예제

import time # 시간제어
import signal # 신호처리, 비동기 이벤트에 대한 핸들러 모듈

def handler(signum, frame): # (인터럽트의 유형/번호, 스택의 정보 출력)
    print('keyboard interupt!!')
    print('signum : ', signum)
    print('stack frame : ', frame)
    exit() # 무한루프 중 인터럽트 발생 시 강제종료

# SIGINT : 키보드 인터럽트 함수
signal.signal(signal.SIGINT,handler)

while True:
    print('Outputting at 5 second intervals...')
    time.sleep(5)