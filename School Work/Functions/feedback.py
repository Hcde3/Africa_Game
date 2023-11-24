f = open("feedback.txt","r")
fs = 0
fp = 0
fn = 0
for l in f:
    fs += 1
    if "Positive" in l:
        fp += 1
    else:
        fn += 1
print(f"Total feedback stored in the file: {fs}\nCount of positive feedbacks: {fp}\nCount of negative feedbacks: {fn}")