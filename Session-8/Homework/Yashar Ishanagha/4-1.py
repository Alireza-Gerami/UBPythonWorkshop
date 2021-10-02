s = input()
lowerc, upperc = 0, 0
for i in s:
    if i >= 'a' and i <= 'z':
        lowerc += 1
         
    if i >= 'A' and i <= 'Z':
        upperc +=1   

if lowerc >= upperc:
    print(s.lower())
else :
    print(s.upper())
    
