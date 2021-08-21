s = input()
su = 0
while True:
    for i in s:
        su+= int(i)
    if su >= 10:
        s = str(su)
        su = 0
    else:
        break
print(su)
