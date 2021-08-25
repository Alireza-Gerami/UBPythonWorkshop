string = input()
uppercase = 0
lowercase = 0
length = len(string)

for i in range(length):
      if(string[i]>='a' and string[i]<='z'):
          lowercase += 1
      elif(string[i]>='A' and string[i]<='Z'):
          uppercase += 1

if lowercase >= uppercase:
	print(string.lower())
else:
	print(string.upper())