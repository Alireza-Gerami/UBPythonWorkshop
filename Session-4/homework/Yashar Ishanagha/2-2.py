n = int(input())
for i in range(1, n+1):
    n = n // 2
    if n%2 != 0:
        break
print(i)

    
