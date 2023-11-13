def Program1(A,B,C):
    if A > B and A > C:
        largest = A
    elif B > A and B > C:
        largest = B
    else:
        largest = C
    return largest

def Program2(A,B,C):
    if A > B:
        if A > C:
            largest = A
        else:
            largest = C
    else:
        if B > C:
            largest = B
        else:
            largest = C
    return largest

def Program3(A,B,C):
    largest = A
    if largest < B:
        largest = B
    if largest < C:
        largest = C
    return largest