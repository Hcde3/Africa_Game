looping = 1
List = []
while looping:
    L = input("Input a number:  ")
    if L == "end":
        looping = 0
    else:
        List.append(int(L))
maximum = 0
for l in List:
    if l > maximum:
        maximum = l
print(maximum)