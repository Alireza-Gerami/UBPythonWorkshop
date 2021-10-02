# https://codeforces.com/contest/1303/problem/A
n = int(input())
for i in range(n):
    s = input()
    a = s.find('1')
    b = s.rfind('1')
    if a == -1:
        print(0)
    else:
        res = s[a:b].count('0')
        print(res)
    