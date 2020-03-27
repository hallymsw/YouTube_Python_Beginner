#
# 1. 실수 두개 입력받기
num1=float(input("num1"))
num2=float(input("num2"))
# 2. 조건문
if num1>=4.0 and num2>=4.0:#4.3 -> T, 3.5 ->F -> T and F -> F
    print("A")
elif num1>=3.0 and num2>=3.0:#4.3 -> T, 3.5 ->T -> T and T -> T
    print("B")
else :
    print("C")
