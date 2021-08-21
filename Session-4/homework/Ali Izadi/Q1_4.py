num = int(input())
a = 1
b = 1
c = 0
if num == 2 or num == 1:
	print(1)
else:
	for i in range(3,num+1):
		c = a + b
		a = b
		b = c

	print(c)