n = int(input())# n>=1
res = 0
while n % 2 == 0:
    n//= 2
    res+=1
print(res)