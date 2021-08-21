s = input()
n = int(input())
for i in range(0, len(s), n):
    print(s[i: i + n])
