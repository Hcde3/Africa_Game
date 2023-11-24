numfile = open("C:\\Users\\19HDaniel.ACC\\Desktop\\function + files\\numbers.txt","r")
total = 0
for line in numfile:
    try: total += int(line.strip())
    except: total += 0
    print(total)