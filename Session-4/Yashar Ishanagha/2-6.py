n = input()
temp = 0
while True:
    for i in n:
        temp1 = int(i)
        temp += temp1
        
    if temp < 10:
        print(temp)
        break
    else:
        n = str(temp)
        temp = 0
