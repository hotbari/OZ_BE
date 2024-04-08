foods = ['불고기와퍼','갈비탕','마라샹궈']

print('참조 주소:',id(foods)) # RAM
print('참조 주소:',hex(id(foods))) # 16진수로

# b는 바이트로 처리한다는 의미
mv = memoryview(b"sungchan")
print(mv)
print(mv[0]) # 바이트 형태로 전달해 유니코드 출력, 인덱스 에러 주의
print(mv[1])
print(mv[2])