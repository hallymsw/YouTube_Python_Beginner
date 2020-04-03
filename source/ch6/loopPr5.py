count=0
sum=0
num=0
# 1. 반복문 : while True:
while True:
    #2. 입력
    num = int(input("점수 입력"))
    #3. 0-100 체크

        #3-1. 0-100
    if num >= 0 and num <=100:
            #누적합, 개수 카운팅
            sum=sum+num
            count=count+1
        #3-2 break
    else:
        break
#4. 합계, 평균 출력
avg=sum/count
print(sum,avg)



    
