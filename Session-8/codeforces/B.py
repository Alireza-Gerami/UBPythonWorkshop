# https://codeforces.com/contest/978/problem/B
n = int(input())
s = input()
res = 0
for i in range(n):
    res+= s[i: i + 3] == 'xxx'
    
print(res)
