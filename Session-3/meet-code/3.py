num = int(input('Enter number: '))
if num % 2 == 0:
    s = input()
    #if s >= 'a' and s <= 'z'
    if 'a'<= s <= 'z' or 'A'<= s <= 'Z':
        print('True')
    else:
        print('False')
else:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if b == 0:
        print('b == 0 Error')
    else:
        print('a / b:', a // b)