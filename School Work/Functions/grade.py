grade = int(input("Grade:  "))
if not grade%10:
    grade += 1
grade_let = 100 - grade
grade_let //= 10
grades = ["A","B","C","D","F","F","F","F","F","F"]
grade_let = grades[grade_let]
print(grade_let)