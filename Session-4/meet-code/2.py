# Question url https://quera.ir/problemset/university/616
n = int(input())
i = 0
while True:
    if 2 ** i > n:
        break
    i += 1
print(2 ** i)
