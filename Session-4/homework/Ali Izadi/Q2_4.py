num = int(input())
count = 0
while True:
	if num % 2 == 0:
		count += 1
	num /= 2
	if num < 2:
		break
		
print(count)