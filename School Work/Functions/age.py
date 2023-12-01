age = int(input("What is your age?:  "))
if age <= 12:
    print("You are a Child")
elif age <= 19:
    print("You are a Teen")
elif age <= 59:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")