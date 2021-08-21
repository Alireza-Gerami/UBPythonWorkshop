h = int(input())
print('.')
c = 0
for i in range(h - 1):
    print('#', '='*c, '*', sep = '')
    c+= 1
    