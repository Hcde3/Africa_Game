f = open("lines.txt","r")
for l in f:
    l = l.strip()
    word = 0
    for i in range(len(l)):
        if l[i] == " ":
            word += 1
    if word >= 8:
        print(l)