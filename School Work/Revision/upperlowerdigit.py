string = input("Input a string: ")
upper = 0
lower = 0
digits = 0
for x in string:
    try:
        int(x)
        digits += 1
    except:
        if x == x.upper():
            upper += 1
        else:
            lower += 1
print(f"Uppercase: {upper}\nLowercase: {lower}\nDigits: {digits}")