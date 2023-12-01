import random
def pos_neg(a):
    if not a:
        return "Zero"
    elif a > 0:
        return "Positive"
    else:
        return "Negative"
num = random.randint(-1,1)
print(f"{num} is {pos_neg(num)}")
