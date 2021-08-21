# https://codeforces.com/contest/58/problem/A
s = input()
t = 'hello'
res = 'YES'
ind = 0
for i in t:
    #i = 'h', 'e'
    ind = s.find(i, ind)
    if ind == -1:
        res = 'NO'
        break
    ind+=1
print(res)
    
    
    