sum=0
count=0
# 1. 반복문(1-> 10)
for i in range(1,21,1):
    # print(i)
    # 2. 총합
    sum=sum+i
    count=count+1
# 3. 더해진 갯수 구하기 -10

# print(count)
# 4. 평균 -> 1번 -> 총합이 정해진때
avg=sum/count
print(avg)