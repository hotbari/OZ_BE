import random

def dice():
	return random.randint(1,5)
	

count = 0

while True:
	a = dice()
	b = dice()
	# print(a,b)
	if a == 3 and b == 3 :
		print(f'A의 주사위 숫자는 {a} 입니다.')
		print(f'B의 주사위 숫자는 {b} 입니다.')
		print('둘이 비겼습니다.')
		print(f'주사위를 굴린 횟수:{count}')
		
		break
	else :
		count += 1
		


