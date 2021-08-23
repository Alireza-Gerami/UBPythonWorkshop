s = input()
c = 0
for i in range(len(s)):
    if s.find(s[i]) < i :
        continue
    else:
        c += 1
print( 'CHAT WITH HER!' if c % 2 == 0 else 'IGNORE HIM!')