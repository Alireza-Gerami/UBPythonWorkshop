number = int(input())
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list = []

for i in range(number):
    str = "-".join(letter[i:number])
    list.append((str[::-1] + str[1:]).center(4 * number - 3, "-"))


for i in reversed(list):
    print(i)

list[::-1]
list.pop(0)
for i in list:
    print(i)