#!/usr/bin/python3
a = int(input())
a1 = a//100
a2 = (a % 100) // 10
a3 = a % 10
print(a1+a2+a3)
print(a3, a2, a1, sep = '')
