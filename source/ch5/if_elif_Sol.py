#1. 점수를 입력
score=int(input("점수 입력"))
#2. 입력받은 정수를 조건식으로 판별
#3. 해당하는 학점을출력
if score >=90 :
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("불합격")
