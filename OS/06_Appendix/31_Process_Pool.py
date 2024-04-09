import concurrent.futures
import time

def task(name):
    time.sleep(0.5)
    return f'{name} is completed.'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor: # 프로세스풀의 프로세스 3개로 설정
        # submit : 실행 함수
        future_name = { executor.submit(task, f'Task-{i}') : f'Task-{i}' for i in range(5) }
        print(future_name)

        '''
        future_name 출력값

        {<Future at 0x1007996d0 state=running>: 'Task-0', 
        <Future at 0x100799af0 state=running>: 'Task-1', 
        <Future at 0x100798bf0 state=running>: 'Task-2', 
        <Future at 0x10079a5a0 state=pending>: 'Task-3', 
        <Future at 0x10079a7e0 state=pending>: 'Task-4'}
        '''

        # 작업이 완료된 순서대로 결과 출력
        for future in concurrent.futures.as_completed(future_name):
            # print(future) <Future at 0x1007996d0 state=finished returned str>
            name = future_name[future]
            try:
                result = future.result()
                print(f'{name}의 결과 : {result}')

            except Exception as e :
                print(e)