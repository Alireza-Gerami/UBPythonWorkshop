n = int(input())
li = []
for i in range(n):
    li.append(input())
    
li = [i.split(' ', 1)[0] for i in li]
count = 0

for i in li:
    if count < li.count(i):
        count = li.count(i)
    for j in li:
        if i in li:
            li.remove(i)
            
print(count)