s = input()
w = int(input())
c = int(0)
s2 = ''
for i in s:
    c += 1
    s2 += i
    if c == w:
        print(s2)
        c = 0
        s2 = ''
print(s2)
