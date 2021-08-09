# Question url https://quera.ir/problemset/university/280
a = int(input())
b = int(input())
c = int(input())
if c < b:
    c, b = b, c
if c < a:
    c, a = a, c

if c ** 2 == a**2 + b**2:
    print("YES")
else:
    print("NO")
