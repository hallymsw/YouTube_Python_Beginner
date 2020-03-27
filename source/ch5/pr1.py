# 1. 키, 몸무게 입력
weight=int(input("몸무게입력"))
height=int(input("키입력"))
# 2. 비만수치 계산
num_ob=weight+100-height
# 3. 비만수치 출력
print(num_ob)
# 4. 비만수치가 0보다 크면 비만이라고 출력
# if 조건식:
#     코드블럭
if num_ob > 0:
    print("obesity")