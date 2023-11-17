string = 'The quick Brow Fox'
def uplowcount(s):
    up = 0
    lw = 0
    for x in range(len(s)):
        if s[x] != " ":
            if s[x] == s[x].upper():
                up += 1
            else:
                lw += 1
    return f"Upper: {up}", f"\nLower: {lw}"

print(*uplowcount(string))