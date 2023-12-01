import random
def evenodd(num):
    if num%2:
        return "Odd"
    else:
        return "Even"
n = random.randint(0,100)
print(f"{n} is {evenodd(n)}")