date = input("Input a date:  ")
day = False
for d in range(len(date)):
    if date[d] == "/":
        if not day:
            day = date[:d]
            slash = d
        else:
            month = date[slash + 1:d]
            year = date[d + 1:]
month = ["January","February","March","April","May","June","July","August","September","October","November","December"][int(month) - 1]
print(f"{month} {day}, {year}")