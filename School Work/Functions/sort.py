n1 = 100
n2 = 6
n3 = 9
L = [n3,n1,n2]
nL = [0,0,0]
for x in L:
    if nL[2] < x:
        nL[0] = nL[1]
        nL[1] = nL[2]
        nL[2] = x
    elif nL[1] < x:
        nL[0] = nL[1]
        nL[1] = x
    else:
        nL[0] = x
    
print(nL)
    