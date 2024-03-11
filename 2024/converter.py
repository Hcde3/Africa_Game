def binary_to_decimal(b):
    b = b[::-1]
    d = 0
    for i,u in enumerate(b):
        d += int(u)*(2**i)
    return d

def decimal_to_binary(d):
    d = int(d)
    b = ""
    while d > 0:
        b = str(d%2) + b
        d //= 2
    return b

def convert(s,mode):
        b = ""
        if mode == "Encode":
            l = [decimal_to_binary(ord(str(x))) for x in s]
            for x in l: b = b + "0" + str(x)
        if mode == "Decode":
            b = [chr(binary_to_decimal(s[x:x+8][1:])) for x in range(0,len(s),8)]
        return b
print(convert("01100001011000100110001101100100011001010110011001100111011010000110100101101010011010110110110001101101011011100110111101110000011100010111001001110011011101000111010101110110011101110111100001111001011110100100000101000010010000110100010001000101010001100100011101001000010010010100101001001011010011000100110101001110010011110101000001010001010100100101001101010100010101010101011001010111010110000101100101011010","Decode"))
            