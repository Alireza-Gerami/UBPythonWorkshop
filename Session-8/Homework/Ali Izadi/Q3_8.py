string = input()
list = []
for i in string:
		if i != '+':
			list.append(i)

list = sorted(list)
list1 = []
for i in list:
	list1.append(i)
	list1.append('+')

list1.pop()
for i in list1:
	print(i,end="")