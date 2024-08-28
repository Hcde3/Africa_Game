L = [4,3,2,1,5,2,4,57,2,42,5,7,82,5,-1]
def bubblesort(l):
    for i in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l.insert(i,l[i+1])
                del l[i+2]
            else:
                i = 0
    return l
print(bubblesort(L))