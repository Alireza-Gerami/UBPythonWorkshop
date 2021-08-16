n = int(input())
a,b,c = 1,1,0
for i in range(3,n+1):
	c = a + b
	a,b = b,c
if n == 1 or n == 2:
    print(a)
else:
    print(c)
	