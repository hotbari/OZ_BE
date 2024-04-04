## pip install psutil
## 프로세스에 대한 추가 기능을 구현하기 위해 설치

## 내 컴퓨터에서 돌아가는 프로세스 조회

import psutil

for proc in psutil.process_iter(): # 프로세스에 반복적으로 접근
    ps_name = proc.name
    # 전부 출력
    # print(ps_name)

    # 크롬의 프로세스만 출력
    if "Chrome" in ps_name() : 
        print(ps_name,'ID is', proc.pid)

