s = input()
r = "".join(dict.fromkeys(s))
if len(r) % 2 == 0:
    print('CHAT WITH HER!')    
else :
    print('IGNORE HIM!')
