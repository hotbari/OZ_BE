# 레퍼런스 카운트가 1인 상태
# 문자열 객체를 변수 my_name이 참조했다
my_name = 'HOTBARI'

# HOTBARI의 레퍼런스 카운트가 2
your_name = my_name

my_name = 'sungchan'
your_name = 'wonbin'

# ----- 레퍼런스 카운트 0 ------ -> 메모리 낭비! 제거대상! [가비지컬렉션]
