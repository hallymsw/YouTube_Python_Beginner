# 1. 두개의 정수를 입력
num1=int(input("첫정수 입력"))#85
num2=int(input("두번째정수 입력")) #50
# 2.어떤수가 큰지 판별
# num1-num2 >0 ->  num1
# num1-num2 <0 -> num2
# 첫번째 입력수가 큰경우
if num1-num2>0: #85-50 -> 35
    num=num1 - num2
    # print(num)
# 그렇지 않은경우
else:## num1-num2 <0 -> num2
    num = num2 - num1 #85 - 50
    # print(num)
# 3. 큰수에서 작은수를 뺀다.
print(num)