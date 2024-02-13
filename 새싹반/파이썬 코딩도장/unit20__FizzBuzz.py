# 3의 배수면 Fizz, 5의 배수면 Buzz, 둘 다 해당되면 FizzBuzz 출력
# for i in range(1,101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print('FizzBuzz')
#     elif i % 5 == 0 :
#         print('Buzz')
#     elif i % 3 == 0 :
#         print('Fizz')
#     else :
#         print(i)

# FizzBuzz 코드 골프
# for i in range(1,101):
#     print('Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 ==0) or i)

# for i in range(1, 101):
#     if (i % 2 == 0) and (i % 11 == 0):
#         print('FizzBuzz')
#     elif i % 2 == 0 :
#         print('Fizz')
#     elif i % 11 == 0 :
#         print('Buzz')
#     else :
#         print(i)
        
        
num1, num2 = map(int, input().split())
for i in range(num1, num2 + 1) :
    if (i % 5 == 0) and (i % 7 == 0):
        print('FizzBuzz')
    elif i % 5 == 0 :
        print('Fizz')
    elif i % 7 == 0 :
        print('Buzz')
    else :
        print(i)