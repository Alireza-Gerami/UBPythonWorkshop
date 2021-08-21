fname, lname = input().split()
if ord(fname[0]) >= 97:
    fname = chr(ord(fname[0]) - 32) + fname[1:]
if ord(lname[0]) >= 97:
    lname = chr(ord(lname[0]) - 32) + lname[1:]
print(fname, lname)
