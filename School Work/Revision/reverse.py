string = input("Input a word: ")
n_string = ""
for x in range(len(string)):
    n_string = n_string + string[-1*x - 1]
print(f"Reverse: {n_string}")