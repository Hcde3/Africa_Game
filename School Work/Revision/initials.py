name = input("Enter your full name:  ")
for x in range(len(name)):
    if not x:
        initials = name[x].upper() + ". "
    if name[x] == " ":
        initials = initials + name[x+1].upper() + ". "
print(initials)
    