import random

def randominrange(x,y):
    return random.randint(x,y)

def asknum():
    ans = input("I am thinking of a number...\nGuess the number:   ")
    return int(ans)

def checkequal(a,b):
    if a == b:
        c = True
    else:
        c = False
    return c

n1 = int(input("Choose a number:\n"))
n2 = int(input("Choose a bigger number:\n"))
comp_num = randominrange(n1,n2)
correct = False
while correct == False:
    answer = asknum()
    correct = checkequal(comp_num,answer)
    if correct == True:
        print("Correct")
    else:
        print("Incorrect")