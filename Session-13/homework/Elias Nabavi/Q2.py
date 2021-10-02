n, a = int(input()), []
for i in range(n):
    x = input().split()
    a.append(x[0])
c, max = set(a), 1
for i in c:
    s = a.count(i)
    if s > max : max = s
print(max)
    
