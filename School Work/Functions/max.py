import random

def maximum(L):
    max_ = L[0]
    for x in L:
        if x >= max_:
            max_ = x
    return max_
        
n1 = random.randint(0,100)
n2 = random.randint(0,100)
print(f"Out of {n1} and {n2}, {maximum([n1,n2])} is the biggest")