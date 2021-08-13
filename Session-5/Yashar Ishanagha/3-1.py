string = input()
stack = []
n = len(string)
for i in string:
    stack.append(i)
for i in range(n):
    print(stack.pop(), end = '')
