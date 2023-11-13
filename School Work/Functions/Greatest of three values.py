import myLibrary
print("This program will Find the Largest of Three Numbers.")
A = int(input("First Number:  "))
B = int(input("Second Number:  "))
C = int(input("Third Number:  "))
ans = input("Choose a program (1, 2 or 3)\n")
if ans == "1":
    largest = myLibrary.Program1(A,B,C)
elif ans == "2":
    largest = myLibrary.Program2(A,B,C)
else:
    largest = myLibrary.Program3(A,B,C)
print(largest,"is the largest number")