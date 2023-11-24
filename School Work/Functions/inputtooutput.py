f = open("input.txt","r")
for l in f:
    l = l.split()
    for i in range(len(l)):
        if l[i][0].upper() != l[i][0]:
            l[i] = l[i][0].upper() + l[i][1:]
    nl = ""
    for x in l:
        nl = nl + x + " "
f = open("wawawa.txt","w")
f.write(nl)
f.close()

f = open("wawawa.txt","r")
for l in f:
    print(l)