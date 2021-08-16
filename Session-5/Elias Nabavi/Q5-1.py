s, n, c = input(), int(input()), 0
for i in s:
    print(i, end = "")    
    c += 1    
    if c >= n :
        c = 0
        print()