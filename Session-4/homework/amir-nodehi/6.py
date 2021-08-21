n = int(input())

s = 0

while True:
    while n != 0:
        s += n % 10
        n //= 10

    if s < 10:
        print(s)
        break

    elif s >= 10:
        n = s
        s = 0
