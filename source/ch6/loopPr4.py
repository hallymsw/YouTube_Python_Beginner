oddCount=0
evenCount=0
num=0
# 1. 반복문 : while True:
while True:
    # 2. 정수입력  , input -> int
    num = int(input("정수 입력"))

    # 3. 0이 입력되면 if -> break
    if num == 0:
        break
    #4. 짝수 홀수 판별
    if num % 2 ==0:
        evenCount=evenCount+1
    else:
        oddCount=oddCount+1



print(evenCount)
print(oddCount)
    


    
