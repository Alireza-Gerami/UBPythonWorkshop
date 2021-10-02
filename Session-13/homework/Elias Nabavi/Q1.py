s = input()
for i in range(len(s)):
    print(s[i]*(i+1),end="")
    print(s[i+1::])