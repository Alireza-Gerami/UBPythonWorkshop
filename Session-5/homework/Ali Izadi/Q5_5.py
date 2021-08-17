s = input()
num = int(input())
num1 = num
j = 0

while True:
    if j > len(s) - num:
        for i in range(j, len(s)):
            print(s[i], end = "")
        break
    else:
        for i in range(j, num1):
            print(s[i], end = "")
            
    j += num;
    num1 += num
    print()