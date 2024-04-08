import tracemalloc

tracemalloc.start()

# 메모리 할당 유발 작업
data = [b'%d' % i for i in range(1,10000)]
joined_data = b' '.join(data) # 공백으로 구분하여 하나의 문자열로 

current, peak = tracemalloc.get_traced_memory() # 현재사용량, 최대사용량

# 메가바이트 단위로 표현하기 위해 10의 6승으로 나눔
print(f'현재 메모리 사용량: {current / 10 ** 6}MB')
print(f'최대 메모리 사용량: {peak / 10 ** 6}MB')

tracemalloc.stop()


# tracemalloc 사용 메모리
traced = tracemalloc.get_tracemalloc_memory()
print(f'추적 중 사용한 메모리: {traced / 10 ** 6}MB')
