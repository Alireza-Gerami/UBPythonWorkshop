n = int(input())
c = 0
while True:
    c += n%10
    n //= 10
    if n < 1 and c < 10:
        c += n
        break
    elif n < 1:
        n,c = c,0
print(c)