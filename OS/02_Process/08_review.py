# 내 파이썬 이름 알아보기

import psutil
import os


if __name__ == '__main__' :
    main_id = os.getpid() #08.py의 프로세스 ID

    for proc in psutil.process_iter(): # 전체 프로세스 조회
        ps_name = proc.name # 프로세스 이름
        ps_id = proc.pid # 프로세스 아이디

        if main_id == ps_id:
            print(f'08.py ID is {main_id}')
            print(f'Process Name: {ps_name}, Process ID: {ps_id}')
        
