string = input("Input a word: ")
palindrome = True
for x in range(len(string)):
    if palindrome:
        if string[x] != string[-1*x - 1]:
            palindrome = False
print(f"Palindrome: {palindrome}")