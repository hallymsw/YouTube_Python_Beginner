# 1. 성별(문자열) 나이(정수)를 입력
gender = input("성별")
age = int(input("나이"))
# 2. 성별
if gender =='M':#남자
# 2-1 나이
    if age >=18: #성인 남자
        print("man")
    else:#미성년 남자
        print("boy")
else:#여자
# 2-1 나이
    if age >= 18:  # 성인 여자
        print("woman")
    else:  # 미성년 여자
        print("girl")
