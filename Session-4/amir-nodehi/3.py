n, m = input().split(' ')
n = int(n)
m = int(m)

s = 1
for i in range(m):
    s *= n
print(s)