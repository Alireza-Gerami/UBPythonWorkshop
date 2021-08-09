# Question url https://quera.ir/problemset/university/9774
s = input()
for i in s:
    print(i, ': ', sep = '', end = '')
    for j in range(int(i)):
        print(i, end = '')
    print()
