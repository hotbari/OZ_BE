import psutil
import os

print("가상메모리의 동작현황-메모리 사용량 조회-")

# psutil.virtual_memory() = 시스템 사용량을 튜플 형식으로 변환해주는 함수
memory_dict = dict(psutil.virtual_memory()._asdict()) # 딕셔너리 형태로 변환
print(memory_dict)
print()

total = memory_dict['total']
available = memory_dict['available']
percent = memory_dict['percent']

print(f'메모리 총량:{total}')
print(f'메모리 즉시 제공 가능량:{available}')
print(f'메모리 사용률:{percent}')
print()
print('-------------------------------------------')

pid = os.getpid()
current_process = psutil.Process(pid) # 20.py에 대한 프로세스로 할당
kb = current_process.memory_info()[0] / 2 ** 20 # 프로세스가 사용한 물리적 메모리의 양을 키로바이트 단위로 변환
print(f'20.py의 메모리 사용량: {kb:.2f} KB')