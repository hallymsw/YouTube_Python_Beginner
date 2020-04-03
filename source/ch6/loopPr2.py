# 1. 반복문 : while True:
while True:

#     2. 입력
    num = int(input("number?"))
#     3. 입력받은수 판별
#         4. 0 -> 반복문 종료 : break
    if num == 0:
        break
#         5. 양수 -> 양수
#         6. 음수 -> 출력
    if num >0:
         print("positive")
    else:
        print("negative")