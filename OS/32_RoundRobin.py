# RoundRobin(프로세스, 프로세스별 실행시간(할당시간), 타임슬라이스)
def RoundRobin(processes, burst_time, time_quantum):

    n = len(processes)
    remaining_time = list(burst_time) 
    turnaround_time = [0] * n # 프로세스 실행되는 시간
    waiting_time = [0] * n # 대기 시간

    time = 0
    queue = []

    while True :
        all_completed = True # 모든 프로세스 종료시 반복문 종료를 위한 플래그

        for i in range(n):
            # 소요시간이 남으면 계속 반복
            if remaining_time[i] > 0:
                all_completed = False

                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    # 작업 함 -> 할당시간 차감
                    remaining_time[i] -= time_quantum
                    queue.append(i)

                else : # 마지막 실행
                    time += remaining_time[i]
                    turnaround_time[i] = time
                    remaining_time[i] = 0
                    waiting_time[i] = turnaround_time[i] - burst_time[i]

        if all_completed :
            break
    
    print('Process\tTurnaround Time\tWating Time')
    for i in range(n):
        print(f'P{i+1}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}')

# 함수 호출
processes = [1,2,3,4,5]
burst_time = [10, 5, 18, 2, 15]
time_slice = 3

RoundRobin(processes,burst_time,time_slice)