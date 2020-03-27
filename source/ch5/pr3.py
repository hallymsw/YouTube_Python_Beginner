# 1. 나이입력
age=int(input("나이입력"))
di=0
# 2. 조건문으로 20비교
#if 조건식:
 #    코드블럭
 # else:
 #    코드블럭
# 2-1 20살 이상인경우 - adult 출력
if age > 20:
    print("adult")
# 2-2 20살 미만 - 20-입력받은 나이를 뺀값 출력
else:
    di=20-age
    print(di,"years later")

