# Question url https://quera.ir/problemset/university/282

n = int(input())
s = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        s+= i
if s == n:
    print('YES')
else:
    print('NO')
