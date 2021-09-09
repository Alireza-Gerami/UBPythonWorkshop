n = int(input())
a = []
for i in range(n):
    flag = False
    s = list(input())
    x = set(s)
    for i in x:
        if s.count(i) > 3 :
            flag = True
            a.append("Ronde!")
            break
    if flag : continue
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            flag = True
            a.append("Ronde!")
            break
    if flag : continue
    if s[0:4:1] == s[7:3:-1]:
        flag = True
        a.append("Ronde!")
    if flag : continue
    a.append("Rond Nist")
for i in a:
    print(i)
        