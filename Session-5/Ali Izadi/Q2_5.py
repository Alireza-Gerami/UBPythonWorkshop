fname, lname = input().split()

a = ord(fname[0])
if 96 < a < 123:
    a -= 32
    
print(chr(a), end = "")
for i in range(1, len(fname)):
    print(fname[i], end = "")

print(' ', end = "")

b = ord(lname[0])
if 96 < b < 123:
    b -= 32
    
print(chr(b), end = "")
for i in range(1, len(lname)):
    print(lname[i], end = "")