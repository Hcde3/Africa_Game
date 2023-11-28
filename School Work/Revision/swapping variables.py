n1 = int(input("Enter an integer:  "))
n2 = int(input("Enter another integer:  "))
print(f"Variable 1: {n1}, Variable 2: {n2}")
n1 = n1/n2
n2 = n1*n2
n1 = n2/n1
n1 = int(n1)
n2 = int(n2)
print(f"Variable 1: {n1}, Variable 2: {n2}")