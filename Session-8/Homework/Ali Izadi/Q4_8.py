'''rows = int(input("Enter the number of rows: "))  
  
k = 2 * rows - 2  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  
  
k = rows - 2  
for i in range(rows, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("") 

        
num = int(input())
num1 = num
num1 += 96
k = 2 * num - 2
for i in range(num):
    for j in range(k):
        print("-",end="")
    k = k - 1
    for j in range(0, i + 1):
        ch = chr(num1)  
        print(ch, end="")
        num1 -= 1
        
    print("")  
    
k = num - 2
for i in range(num, -1, -1):  
    for j in range(k, 0, -1):  
        print("-",end="")  
    k = k + 1  
    for j in range(0, i + 1):  
        print(ch, end="") 
    print("") '''
    
    
num = int(input())
list = ['a','b','c','d','e','f','g','h','i','j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
j = 1
num1 = num
k = 2 * num - 1
for i in range(1,len(list)):
    for j in range(1, k):
        print('-', end="")
    print(chr(num + 96), end="")
    for j in range(1, k):
        print('-', end="")
    
    k -= 2
    a = 1
    x = 1
    while True:
        for s in range(k):
            print('-', end="")
        while True:
            print(chr(num + 96),'-', end="")
            
            for f in range(a):
                print(chr(num + 96 - x),'-', end="")
            x += 1
            a += 2
            print(chr(num + 96), end="")
    print() 

