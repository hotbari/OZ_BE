import random
rsp = ['주먹','가위','보']

def who_win(x,y):
	if x == "가위" :
		if y == "가위" :
			msg = "무승부"
		elif y == "바위" :
			msg = "상대의 승리"
		else :
			msg = "나의 승리"
	elif x == "바위" :
		if y == "바위" :
			msg = "무승부"
		elif y == "보위" :
			msg = "상대의 승리"
		else :
			msg = "나의 승리"
	else:
		if y == "보" :
			msg = "무승부"
		elif y == "가위" :
			msg = "상대의 승리"
		else :
			msg = "나의 승리"
			
	return msg
	
print("=" * 30)
print("가위바위보 게임")
print("=" * 30)

again = 'y'
while again == 'y':
	me = random.choice(rsp)
	you = random.choice(rsp)

	result = who_win(me, you)
	print("나 : %s"%me)
	print("상대 : %s"%you)
	print(result)
	print("=" * 30)
	
	break
	
print("게임종료")