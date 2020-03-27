#1. 점수를 입력
score=int(input("점수 입력"))

if score >=90 :
    if score >= 95:
        print("A+")
    else:#90점 이상
        print("A-")
elif score >=80:

    if score >= 85:
        print("B+")
    else:#80점 이상
        print("B-")
elif score >=70:
    if score >= 75:
        print("C+")
    else:#70점 이상
        print("C-")
elif score >=60:
    if score >= 65:
        print("D+")
    else:#60점 이상
        print("D-")
else:
    print("불합격")
