mass = int(input("What is your kg:  "))
height = float(input("What is your height in metres:  "))
BMI = mass/(height**2)
print(f"BMI: {BMI}")
if BMI <= 18.5:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are a normal weight")
elif BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese")
