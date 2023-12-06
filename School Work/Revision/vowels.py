string = input("Input a word: ")
vowels = 0
for x in string:
    if x in "aeiou":
        vowels += 1
print(f"Vowels: {vowels}")