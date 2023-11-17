string = "1234abcd"
def reverse(s):
    ns = ""
    for x in range(len(s)):
        ns = ns + s[-x-1]
    return ns
print(reverse(string))