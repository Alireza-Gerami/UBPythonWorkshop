num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
mul = 1
for i in range(1, num2+1):
	mul *= num1
	
print(mul)