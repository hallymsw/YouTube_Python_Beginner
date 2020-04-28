#2개의 값을 입력받아서 4칙연산을 해서 결과값 4개를 리턴
def calculate(x,y):
    sum=x+y
    sub=x-y
    div=x/y
    mul=x*y
    return (sum, sub, div, mul)

x=1
y=10
sum=sub=div=mul=0
sum, sub, div, mul=calculate(x,y)#11 -9 0.1 10
print(sum, sub, div, mul)


