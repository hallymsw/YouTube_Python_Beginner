def get_square(i):
    global res
    res=i**2
    print("inner : ", res)
n=2
res=0
get_square(n)
print("outter : ", res)