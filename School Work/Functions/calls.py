calls = int(input("Input number of calls:  "))
total = 200
if calls > 100:
    calls -= 100
    if calls > 50:
        total += 30
        calls -= 50
        if calls > 50:
            total += 25
            total += calls*0.4
        else:
            total += calls*0.5
    else:
        total += calls*0.6
print(total)