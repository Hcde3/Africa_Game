looping = 1
List = []
while looping:
    L = input("Input a number:  ")
    if L == "end":
        looping = 0
    else:
        List.append(L)
nL = [List[-1]]
for i in List:
    if i != List[-1]:
        nL.append(i)
print(nL)