import math
a = int(input("Length of size 1:  "))
b = int(input("Length of size 2:  "))
c = int(input("Length of size 3:  "))
s = (a+b+c)/2
a = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area: {a}")