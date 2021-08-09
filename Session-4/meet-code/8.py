# Question url https://quera.ir/problemset/university/593

n = int(input())
b = 0
N = n
while N > 0:
    b+= N % 10
    N//= 10
#print(b)

tmp = n + 1
t = 0
while True:
    c = 0
    for i in range(1, tmp // 2 + 1):
        if tmp % i == 0:
            c+= 1
    if c == 1:
        t+= 1
        if t == b:
            print(tmp)
            break
        else:
            pass
        tmp+= 1
    else:
        tmp+= 1










