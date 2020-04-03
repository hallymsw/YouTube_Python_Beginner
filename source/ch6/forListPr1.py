A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
count=0
# 1.반복문을 이용 요소를 가져오고
for i in A :
    print(i)
    # 2. 총합을 구하고
    sum=sum+i
    # 3. 더해진 갯수
    count=count+1

# 4. 평균을 구한다
avg=sum/count
print(avg)