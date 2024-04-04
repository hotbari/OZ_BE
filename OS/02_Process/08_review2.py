# 내 파이썬 이름 알아보기

import psutil
import os

# 함수화
def print_process_detail():
    for proc in psutil.process_iter():
        ps_name = proc.name
        ps_id = proc.pid

        if main_id == ps_id:
            print(f'08.py ID is {main_id}')
            print(f'Process Name: {ps_name}, Process ID: {ps_id}')


if __name__ == '__main__' :
    main_id = os.getpid() #08.py의 프로세스 ID

    print_process_detail()

    
    
