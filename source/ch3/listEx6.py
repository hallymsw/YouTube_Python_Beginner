a = [1, 2, 4]
lVal=a[1:2]
print(lVal)
# [1, ['a', 'b', 'c'], 4]
#[1, 'a', 'b', 'c', 4]
a[1:2]=['a','b','c']
print(a)