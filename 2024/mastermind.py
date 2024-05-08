import random
import colorama

colorama.init(autoreset=True)
from colorama import Fore, Back, Style

newpage = "\n"*11

print("MASTERMIND")
print("\nGuess 4 colours from a randomly generated list of 4 colours. Use first letter of the colour, valid colours are: (r)ed,(o)range,(y)ellow,(g)reen,(b)lue,(p)urple,(w)hite")
print("Your guesses will be returned in the format:")
print(Fore.GREEN + "Correct position,",Fore.YELLOW + "In list but wrong position,",Fore.RED + "Not in list","and",Fore.MAGENTA + "In list but guessed too many times")
input("\nType anything to start")
print(newpage)
guesses = 0
rcol = []
gcol = []
x = 0
while x < 4:
    Colours = ["r","o","y","g","b","p","w"]
    rcol.append(random.choice(Colours))
    x += 1
tries = 0
x = 0
correct = False
while not correct:
    z = 0
    while z < 4:
        VALID = 0
        while not VALID:
            incol = input("\nGuess a colour\n").lower()
            if incol in Colours:
                VALID = True
            else:
                print("Invalid input. Try again.")
        gcol.append(incol)
        z += 1
    correctcol = []
    wrongpos = []
    wrongcol = []
    tmt = []
    preslist = []
    print(newpage)
    while x < 4:
        c = gcol[x]
        if c in rcol:
            if c == rcol[x]:
                preslist.append(("C",c))
            else:
                if gcol.count(c) > rcol.count(c):
                    preslist.append(("T",c))
                else:
                    preslist.append(("W",c))
        else:
            preslist.append(("N",c))
        x += 1
    for z in preslist:
        if z[0] == "C":
            print(Fore.GREEN + f"{z[1]}", end = ', ')
        if z[0] == "T":
            print(Fore.MAGENTA + f"{z[1]}", end = ', ')
        if z[0] == "W":
            print(Fore.YELLOW + f"{z[1]}", end = ', ')
        if z[0] == "N":
            print(Fore.RED + f"{z[1]}", end = ', ')
    if gcol == rcol:
        correct = True
    else:
        gcol = []
        x = 0
        tries += 1
print(Fore.CYAN +f"\nYou won after {tries} tries!")
