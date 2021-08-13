n = input()
a = ''
for i in range(0,len(n)):
    if i == 0 or n[i-1] == " ":
        if 'a' <= n[i] <= 'z' :
            a += chr(ord(n[i]) - 32)
        else:
            a += n[i]
    else:
        a += n[i]
print(a)