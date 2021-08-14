num = int(input())
div = 0

if num < 10:
    print(num)
else:
    while num >= 1 or div >= 10:
        if num == 0:
            num = div
            div = 0
        div += num % 10
        num //= 10
    
    print(div)