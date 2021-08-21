n, m = input().split(' ')
n = int(n)
m = int(m)
temp = n
for i in range(1, m):
    n *= temp
print(n)
