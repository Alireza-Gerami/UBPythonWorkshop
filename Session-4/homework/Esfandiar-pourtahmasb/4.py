a = int(input())
b = int(input())
for i in range(a, b + 1):
    flag = False
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = True
            break
    if flag == False and i != 1:
        print(i)
    