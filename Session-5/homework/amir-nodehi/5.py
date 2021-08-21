s = input()
w = int(input())

for i in range(1, len(s)+1):
    print(s[i-1], end='')
    if i % w == 0:
        print()
