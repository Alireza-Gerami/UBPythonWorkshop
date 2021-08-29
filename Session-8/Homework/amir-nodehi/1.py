s = input()

low = 0
up = 0

for i in s:
    if i.islower():
        low += 1
    else:
        up += 1
if low >= up:
    print(s.lower())
else:
    print(s.upper())
