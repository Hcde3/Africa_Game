file = open("C:\\Users\\19HDaniel.ACC\\Desktop\\function + files\\shelley.txt","r")
blank = 0
full = 0
for line in file:
    if line.strip() == "":
        blank += 1
    else:
        full += 1
print(f"Empty Lines: {blank}\nNon-Empty Lines: {full}")
file.close()
    
    