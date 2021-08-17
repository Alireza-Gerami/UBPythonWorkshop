n = int(input())
f1 = 1
f2 = 1
if n == 1 or n == 2:
    print(1)
else:
    for i in range(n-2):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    print(f3)
