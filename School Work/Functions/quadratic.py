import math
a = int(input("Input Coefficient of x^2:	"))
b = int(input("Input Coefficient of x:	"))
c = int(input("Input Constant:	"))

dis = b**2 - (4*a*c)
print("\n")
if not dis:
    print("Equal Roots")
elif dis > 0:
    print("2 Real Distinct Roots")
elif dis < 0:
    print("2 complex Distinct Roots")
    
neg_root = (-b - math.sqrt(dis))/(2*a)
pos_root = (-b + math.sqrt(dis))/(2*a)

print(f"Roots: x = {neg_root}, x = {pos_root}")