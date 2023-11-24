filename = input("Choose a file name:  ")
filecontent = input("Choose what to write:\n")
filename = filename + ".txt"
f = open(filename,"w")
f.write(filecontent)
f.close()