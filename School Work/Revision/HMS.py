s = int(input("Input time in seconds:  "))
h = s//3600
m = (s%3600)//60
s = s%60
print(f"Hours: {h}h\nMinutes: {m}m\nSeconds: {s}s")