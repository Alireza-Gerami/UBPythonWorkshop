n = int(input())
Array = list(map(int, input().split(' ')[:n]))

Array.sort()
min = 100
k = 1
list = []
for i in Array:
    if min > Array.count(i):
        min = Array.count(i)
        k = i
print(k) 