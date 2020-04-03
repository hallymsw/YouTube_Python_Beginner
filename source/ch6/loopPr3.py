avg=0
num=0
sumData=0
count=0
# 1. 반복문 : while True:
while True:
    #2. 정수 입력
    num = int(input("정수 입력"))

    #3. 누적합을 구함
    sumData=sumData+num
    count=count+1

    # 4. 100이상인 판별 : 반복문 종료
    if num >= 100:
        break


print(sumData)
avg=sumData/count
print(avg)



    
