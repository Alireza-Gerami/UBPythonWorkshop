n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
    
def reverse(n):
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10 
    return rev

def divide(n):
    for i in range(len(str(n)) - 2):
        for j in range(10):
            if str(n)[i:i+3].count(str(j)) == 3:
                return True
        
j = 0
while True:
    if j >= n:
        break
    array = [int(x) for x in str(list[j])]
    res = False
    for i in array:
        if array.count(i) >= 4:
            res = True
        elif divide(list[j]) == True:
            res = True
        elif list[j] == reverse(list[j]):
            res = True
    
    j += 1
    if res == True:
        print('Ronde!')
    else:
        print('Rond Nist')
        