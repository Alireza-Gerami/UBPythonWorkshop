h = int(input())

print('.')
for i in range(1, h):
    print('#', end='')
    if i > 1:
        a = i - 1
        b = a * '='
        print(b, end='')
        print('*')
    else:
        print('*')
