import random

def Addition():
    n1 = random.randint(5,20)
    n2 = random.randint(5,20)
    a = input("Add " + str(n1) + " and " + str(n2) + " together\n")
    a = int(a)
    return a, n1+n2

def Subtraction():
    n1 = random.randint(5,20)
    n2 = random.randint(5,20)
    a = input("Subtract " + str(n1) + " from " + str(n2) + "\n")
    a = int(a)
    return a, n2-n1
def checkequal(a,b):
    if a == b:
        c = True
    else:
        c = False
    return c

ans = input("1) Addition\n2) Subtraction\nEnter 1 or 2: ")
if ans == "1" or ans == "2":
    if ans == "1":
        nums = Addition()
    else:
        nums = Subtraction()
    print("Your Answer:",nums[0],"\nActual Answer:",nums[1])
    correct = checkequal(nums[0],nums[1])
    if correct == False:
        print("Incorrect")
    else:
        print("Correct")
else:
    print("Incorrect Input")