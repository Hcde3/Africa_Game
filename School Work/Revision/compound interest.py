p = int(input("Input the Principle:  "))
r = int(input("Input the Rate:  "))
t = int(input("Input the Time:  "))
i = (p*(1+(r/100))**t) - p 
print(i)