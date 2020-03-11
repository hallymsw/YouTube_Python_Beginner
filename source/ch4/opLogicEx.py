result=(10 == 10 and 10 != 5)
#10은 10과 같다-> T
#10은5와 같지않다 -> T
#T and T-> True
print(result)

result=(10 > 5 or 10 < 3)
#10은 5보다 크다 -> T
#10은 3보다 작다 -> F
#T or F -> T
print(result)

result=not (10 > 5)
#10은 5보다 크다 -> T
#not T -> F
print(result)
