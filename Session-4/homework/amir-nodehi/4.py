a = int(input())
b = int(input())

s = 0
for i in range(a, b+1):
    for j in range(2, i+1):
        if i % j == 0:
            s += 1

    if s == 1:
        print(i)
    s = 0
