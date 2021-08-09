# Question url https://quera.ir/problemset/university/591

n = int(input())
if n == 1:
    print('*')
else:
    for i in range(n):
        print('*', end = '')
    print()
    for i in range(n - 2):
        print('*', end = '')
        for j in range(n - 2):
            print(' ', end = '')
        print('*')
    for i in range(n):
        print('*', end = '')
    print()
