numbs = input("Input a 10 digit number: ")
odds = []
for i in range(len(numbs)):
    if int(numbs[i])%2:
        odds.append(i)
print(*odds, sep=",")
        
        