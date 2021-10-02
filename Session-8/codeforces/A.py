# https://codeforces.com/contest/734/problem/A
input()
s = input()
a = s.count('A')
d = s.count('D')
print('Anton' if a > d else 'Danik' if d > a else 'Friendship')