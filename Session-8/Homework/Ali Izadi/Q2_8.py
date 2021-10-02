string = input()
list = []
for i in string:
	if i not in list:
		list.append(i)
		
if len(list) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")