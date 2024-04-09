number = 99

# n진수 반환
# 문자열 X
print('bin 99 is ', bin(number)) # 0b-10진수가 아니라는 표시 1100011
print('oct 99 is ', oct(number)) # 0o 143
print('hex 99 is ', hex(number)) # 0x63

bin_num = bin(number)
print(hex(int(bin_num[2:]))) # hex(1100011)
