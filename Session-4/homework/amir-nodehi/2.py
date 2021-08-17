n = int(input())
s = 0
while n % 2 == 0:
    n /= 2
    s += 1
print(s)
