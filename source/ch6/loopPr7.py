num=0
sum=0
# 1. 입력
num=int(input("정수입력"))
# 2. 반복문 for range
for i in range(1,num+1,1):
#     3. 변수 체크 -> 5의 배수면 누적합 더하기
    if i%5==0:
        sum=sum+i
# 4. 누적합 을 출력
print(sum)
    





    
