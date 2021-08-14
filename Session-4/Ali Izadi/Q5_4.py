num = int(input())
for i in range(1,num+1):
    if i == 1:
        print('.')
    elif  i == 2:
        print('#*')
    else:
        print('#', end = '')
        for j in range(3, i+1):
            print('=', end = '')
        print('*')