s = input()

count = 0
chars = ''

for i in s:
    if i not in chars:
        chars += i

if len(chars) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')