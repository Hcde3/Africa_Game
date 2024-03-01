def AND(a,b):
    return a*b

def OR(a,b):
    if a or b: return 1
    else: return 0

def NOT(a):
    if a: return 0
    else: return 1

def NAND(a,b):
    return NOT(AND(a,b))

def NOR(a,b):
    return NOT(OR(a,b))

def XOR(a,b):
    return OR(AND(a,NOT(b)),AND(b,NOT(a)))

def XNOR(a,b):
    return NOT(XOR(a,b))

def Half_Adder(a,b):
    return [XOR(a,b),AND(a,b)]

def Full_Adder(a,b,c):
    return [XOR(XOR(a,b),c),OR(AND(a,b),AND(XOR(a,b),c))]

def Adder(bin1,bin2):
    bin1 = list(bin1[::-1])
    bin2 = list(bin2[::-1])
    while len(bin1) < len(bin2):
        bin1.append("0")
    while len(bin2) < len(bin1):
        bin2.append("0")
    carry = 0
    output = ""
    for i in range(len(bin1)):
        fa = Full_Adder(int(bin1[i]),int(bin2[i]),carry)
        carry = fa[1]
        output = str(fa[0]) + output
    if carry: output = str(carry) + output
    return output

choice = input("(G) Gates\n(B) Binary Adder\n")
if choice == "G":
    gate_info = [("NOT","\n| A | Q |\n| 1 | 0 |\n| 0 | 1 |"),("AND","\n| A | B | Q |\n| 1 | 1 | 1 |\n| 1 | 0 | 0 |\n| 0 | 1 | 0 |\n| 0 | 0 | 0 |"),("OR","\n| A | B | Q |\n| 1 | 1 | 1 |\n| 1 | 0 | 1 |\n| 0 | 1 | 1 |\n| 0 | 0 | 0 |"),("NAND","\n| A | B | Q |\n| 1 | 1 | 0 |\n| 1 | 0 | 1 |\n| 0 | 1 | 1 |\n| 0 | 0 | 1 |"),("NOR","\n| A | B | Q |\n| 1 | 1 | 0 |\n| 1 | 0 | 0 |\n| 0 | 1 | 0 |\n| 0 | 0 | 1 |"),("XOR","\n| A | B | Q |\n| 1 | 1 | 0 |\n| 1 | 0 | 1 |\n| 0 | 1 | 1 |\n| 0 | 0 | 0 |"),("XNOR","\n| A | B | Q |\n| 1 | 1 | 1 |\n| 1 | 0 | 0 |\n| 0 | 1 | 0 |\n| 0 | 0 | 1 |")]
    ans = int(input("Choose a gate:\n1. NOT\n2. AND\n3. OR\n4. NAND\n5. NOR\n6. XOR\n7. XNOR\n"))
    tos = input("Would you like to see the truth table or do a sum? (answer t or s)\n")
    for i, g in enumerate(gate_info):
        if i+1 == ans:
            if tos == "t":
                print(g[1])
            else:
                a = int(input("Input first digit:\n"))
                if i: b = int(input("Input second digit:\n"))
                if g[0] == "NOT":
                    c = NOT(a)
                if g[0] == "AND":
                    c = AND(a,b)
                if g[0] == "OR":
                    c = OR(a,b)
                if g[0] == "NAND":
                    c = NAND(a,b)
                if g[0] == "NOR":
                    c = NOR(a,b)
                if g[0] == "XOR":
                    c = XOR(a,b) 
                if g[0] == "XNOR":
                    c = XNOR(a,b) 
                if i: print(f"{a} {g[0]} {b} is {c}")
                else: print(f"{g[0]} {a} is {c}")
else:
    bin1 = input("Input first binary number:\n")
    bin2 = input("Input second binary number:\n")
    print(Adder(bin1,bin2))
