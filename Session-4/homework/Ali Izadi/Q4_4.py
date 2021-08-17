num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
	if i == 1:
		continue
	a = True
	for j in range(2, i // 2 + 1):
            if i % j != 0:
                continue
            else:
                a = False
                break
                
	if a == True:
		print(i)