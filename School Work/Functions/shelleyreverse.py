f = open("shelley.txt","r")
lines = []
n = 0
for l in f:
    l = l.strip()
    lines.append(l)
for x in range(len(lines)):
    n = x+1
    print(lines[-n])