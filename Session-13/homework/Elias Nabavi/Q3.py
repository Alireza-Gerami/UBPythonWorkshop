n = int(input())
a = list(map(int,input().split()))
c, min, x = list(set(a)), 101, 101
c.sort()
for i in c:
    s = a.count(i)
    if s < min:
        min = s
        x = i
print(x)