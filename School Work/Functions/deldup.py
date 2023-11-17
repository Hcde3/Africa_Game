List = [1,2,3,3,3,3,4,5]
def deldup(l):
    nl = []
    for x in l:
        if not x in nl:
            nl.append(x)
    return nl
print(deldup(List))