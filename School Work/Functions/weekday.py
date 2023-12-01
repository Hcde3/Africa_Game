import random
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
num = random.randint(1,7)
day = days[num-1]
print(f"Day {num} is {day}")