List = [8, 2, 3, -1 , 7]
def sumof(l):
    p = 1
    for x in l:
        p *= x
    return p
print(sumof(List))