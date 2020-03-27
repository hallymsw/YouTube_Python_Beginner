#
# 1. 실수 입력받기
num=float(input("실수입력"))
# print(type(num))
# 2. 조건문에서 범위체크
# 2-1 문자열출력
if num >=4.0:
    print("scholarship")
elif num >=3.0:
    print("next semeser")
elif num >=2.0:
    print("seasonal semeser")
else:
    print("retake")
