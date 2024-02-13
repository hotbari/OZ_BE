import turtle as t

# n = int(input("n각형을 만듭니다. n을 입력하세요."))
# t.shape('turtle')

# for i in range(n):
#     t.fd(100)
#     t.right(360/n)


# 오각별 그리기
# for i in range(5):
#     t.fd(100)
#     t.right(144)
#     t.fd(100)
#     t.left(72)

# 꼭지점갯수 n, 선분 길이 line 받아서 별 그리기

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.fd(line)
    t.right((360/n)*2)
    t.fd(line)
    t.left(360/n)
    

# 터틀창 종료 막는 모듈
t.mainloop()
# t.exitonclick()



