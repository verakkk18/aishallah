#!/usr/bin/python3
s = input()
t = input()

n = len(s)
m = len(t)

p = list()

for i in range ( n - m + 1):
    if s[i:i+m] == t:
        p.append(i+1)

print (*p)
