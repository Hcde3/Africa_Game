file = open("C:\\Users\\19HDaniel.ACC\\Desktop\\function + files\\shelley.txt","r")
r1 = int(input("Pick a starting line:  "))
r2 = int(input("Pick an ending line:  "))
n = 0
for line in file:
    n += 1
    if n >= r1 and n <= r2: print(line)
file.close()
    
    