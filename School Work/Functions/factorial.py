num = 5
def factorial(n):
    f = 1
    for x in range(n):
        f *= x+1
    return f
print(factorial(num))