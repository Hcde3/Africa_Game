def validate(P):
    valid = False
    if len(P) >= 8:
        capital = False
        lower = False
        digit = False
        for x in P:
            try:
                int(x)
                digit = True
            except:
                if x == x.upper():
                    capital = True
                else:
                    lower = True
        if digit and capital and lower:
            valid = True
    return valid

valid = False
msg = ""
while not valid:
    print(msg)
    password = input("Input a password:  ")
    valid = validate(password)
    msg = "\nInvalid, try again\n"
print("\nPassword set")