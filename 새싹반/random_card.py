import random

cards = ['A-d(a-dia)', 'A-c(a-clover)', 'A-h(a-heart)', 'A-s(a-space)']
result = random.choice(cards)

def card_result():
	num = 0
	if result == 'A-d(a-dia)':
		num = 1
	elif result == 'A-c(a-clover)':
		num = 2
	elif result == 'A-h(a-heart)':
		num = 3
	else :
		num = 4
		
	print(f'random card change result = {num}')
	
card_result()
	