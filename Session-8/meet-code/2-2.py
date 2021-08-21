n = int(input())
counter = 0
while 1:
    if n % 2 != 0:
        break
    n //= 2
    counter += 1
print(counter)

