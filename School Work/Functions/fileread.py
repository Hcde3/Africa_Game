fin = open("C:/Users/19HDaniel.ACC/Desktop/function + files/Filetest.txt",'r')

for line in fin:
    print(line.strip())
    
fin.close()