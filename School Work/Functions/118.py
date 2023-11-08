def numinput():
    x = input("Enter a number:\n")
    return int(x)

def countup(i):
    for x in range(i):
        print(x+1)

num = numinput()
countup(num)