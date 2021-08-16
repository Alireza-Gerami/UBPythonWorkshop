s = input()

c = 0
for i in range(len(s)):
    if s[i] == chr(32):
        c += 1
print(c+1)
