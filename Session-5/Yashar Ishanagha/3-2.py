name, lastname = input().split()
firstchar = name[0]
flag = True
flag2 = True

for i in range(97, 122 + 1):
    if i == ord(firstchar):
        temp = i - 96
        for j in range(65, 90 + 1):
            asciicode = j
            temp2 = j - 64
            if temp2 == temp:
                capital = chr(asciicode)
                print(capital, end = '')
                flag = False
if flag == True:
    print(firstchar, end = '')       
length = len(name)
for k in range(1, length):
    print(name[k], end = '')

print(end = ' ')

firstchar = lastname[0]
for i in range(97, 122 + 1):
    if i == ord(firstchar):
        temp = i - 96
        for j in range(65, 90 + 1):
            asciicode = j
            temp2 = j - 64
            if temp2 == temp:
                capital = chr(asciicode)
                print(capital, end = '')
                flag2 = False
if flag2 == True:
    print(firstchar, end = '')
length = len(lastname)
for k in range(1, length):
    print(lastname[k], end = '')
