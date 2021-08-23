s = input()
a,b,c = 0,0,0
for i in range(len(s)):
    if s[i] == '1':
        a += 1
    elif s[i] == '2':
        b += 1
    elif s[i] == '3':
        c += 1
if b == 0 and c == 0:
    print( '1+'*(a-1) , sep = '', end = '' )
    if a > 0: print('1', end = '')
elif c == 0:
    print( '1+'*a , '2+'*(b-1) , sep = '', end = '' )
    if b > 0: print('2', end = '')
else:
    print( '1+'*a , '2+'*b , '3+'*(c-1), sep = '', end = '' )
    if c > 0: print('3', end = '')