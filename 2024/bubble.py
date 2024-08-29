import colorama
colorama.init(autoreset=True)
from colorama import Fore, Back, Style

L = []
length_list = int(input("How many numbers in list?\n"))
for choice in range(length_list): L.append(int(input("Add a number:\n"))) #user centred design to allow the user to choose the list


def smartprint(l,i, swap): #user centred design to communicate which numbers are bubbled
    print("[",end = "")
    for ind, prnt in enumerate(l):
        en = ", "
        if ind == 0:
            prnt = str(prnt)
        if ind == len(l)-1:
            en = "]\n"
        if ind == i:
            print(Back.YELLOW + str(prnt),end = en)
        elif ind == i + 1:
            if swap: print(Back.GREEN + str(prnt),end = en)
            else: print(Back.RED + str(prnt),end = en)
        else:
            print(str(prnt),end = en)

def bubblesort(l):
    for p in range(len(l) - 1):
        print(f"Pass {p+1}")
        swapping = True
        pass_add = True
        for i in range(len(l) - 1):
            if pass_add:
                i += p
                pass_add = False
            if swapping:
                if l[i] > l[i + 1]:
                    smartprint(l,i,True)
                    l.insert(i,l[i+1])
                    del l[i+2]
                    print(l,"SWAP")
                else:
                    smartprint(l,i,False)
                    print(l,"NO SWAP")
                    swapping = False
    return l
print("Sorted List:",Back.BLUE + str(bubblesort(L)))
