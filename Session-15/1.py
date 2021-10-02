l = [str(65651),'alireza\n', 'mohmmad\n', 'reza\n', 'sara\n', 'neda\n']
# file = open('./username.txt','w')
# file.write('mina')
# # for user in l:
# # 	file.write(f'{user}\n')
# file.writelines(l)
# file.close()


# file = open('./username.txt','a')
# file.write('mina')
# file.write('amir')
# file.write('zahra')
# file.close()

# file = open('username.txt', 'r')
# # all_file = file.read()
# # print(all_file)
# # print(type(all_file))

# lines = file.readlines()
# print(lines)
# print(type(lines))


# lines = file.readlines()
# print(lines)
# print(type(lines))
# file.close()

with open('./username.txt','w') as fw:
	fw.write('wrtie in with block')
	fw.write('wrtie in with block')
	fw.write('wrtie in with block')
	fw.write('wrtie in with block')
	fw.write('wrtie in with block')


with open('./username.txt','a') as fa:
	fa.writelines(l)

with open('username.txt', 'r') as fr:
	print(fr.read())


with open('username.txt', 'r+') as fr:
	print(fr.read())
	fr.write('adgadg')
	fr.writelines(l)
