f = open("badSpelling.txt","r")
for l in f:
    w = l.split()
    for i in w:
        try: int(i[-1]); print(i)
        except: None