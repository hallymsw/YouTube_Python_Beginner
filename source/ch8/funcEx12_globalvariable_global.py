
def get_square(i):
    global res
    res=i**2
    print("inner",res)

y=2
res=0
get_square(y)
print("outter",res)


