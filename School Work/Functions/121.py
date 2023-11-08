def add():
    nn = input("Enter a name to add\n")
    return nn
def edit():
    complete = 0
    while complete == 0:
        on = input("Choose a name to edit\n")
        nn = input("Choose a new name\n")
        for i in range(len(names)):
            if on == names[i]:
                names[i] = nn
                complete = 1
        if complete != 1:
            print("Incorrect input")
def delete():
    complete = 0
    while complete == 0:
        on = input("Choose a name to delete\n")
        for i in range(len(names)):
            if complete != 1:
                if on == names[i]:
                    names.remove(on)
                    complete = 1
        if complete != 1:
            print("Incorrect input")
def newpg():
    for x in range(10):
        print("\n")
    

    

ongoing = True
while ongoing == True:
    loop = True
    names = []
    while loop == True:
        newpg()
        for x in range(len(names)):
            print(x+1,names[x])
        print("\nCommands: \na = Add \ne = Edit \nd = Delete \nr = Restart \nf = Finish")
        cmd = input("\nInput a command\n")
        if cmd == "a":
            names.append(add())
            newpg()
        elif cmd == "e":
            edit()
            newpg()
        elif cmd == "d":
            delete()
            newpg()
        elif cmd == "f":
            newpg()
            for x in range(len(names)):
                print(x+1,names[x])
            ongoing = False
            loop = False
        elif cmd == "r":
            newpg()
            loop = False