s = input()
u, d = 0, 0
for i in range(len(s)):
    if ord(s[i]) >= 97 and ord(s[i]) <= 122 :
        d += 1
    elif ord(s[i]) >= 65 and ord(s[i]) <= 90 :
        u += 1
print( s.lower() if d>=u else s.upper() )