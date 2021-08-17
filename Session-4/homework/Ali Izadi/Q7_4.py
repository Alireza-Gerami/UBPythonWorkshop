num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
count = 0

for i in range(num1, 0, -1):
    if (num1 == 0):
        break
   
    if num1 % 10 == num2:
        count += 1
    num1 //= 10
print(count)