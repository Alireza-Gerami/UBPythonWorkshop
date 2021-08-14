n, m = input().split()
n = int(n)
m = int(m)

count = 0

while n != 0:
    if n%10 == m:
        count += 1
    n //= 10 

print(count)