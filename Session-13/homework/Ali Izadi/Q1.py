n = input()
print(n)
k = 1

for i in range(1,len(n)):
    
    for j in range(0,i):
        print(n[k],end="")
        
    k += 1
    print(n[i:])