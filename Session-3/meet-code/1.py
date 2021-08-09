for i in range(1, 11):
    for j in range(1, 11):
        if i * j >= 10:
            print(i * j, end = ' ')
        else:
            print(i * j, end = '  ')
    print()