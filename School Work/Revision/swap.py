string = input("Input a word: ")
string = string[-1] + string[1:-1] + string[0]
print(f"{string}")