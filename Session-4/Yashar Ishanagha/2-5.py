h = int(input())
print('.')
for i in range(2, h + 1):
    print('#',end = '')
    for j in range(i - 2):
        print('=', end = '')
    print('*')
