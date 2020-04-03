count =0
num=0
# 1. 반복문 : while True:
while True:
    # 2. 정수 입력
    num= int(input("정수 입력"))

    #3. 0입력되면 반복문 종료
    if num ==0:
        break
    count=count+1
    #4. 3의 배수, 5의 배수 아닌것 카운팅 제외
    if num %3==0 or num %5==0:
        count = count - 1
print(count)








    
