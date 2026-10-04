#!/usr/bin/python3
a = int(input())
ch = a // 3600
mi = (a % 3600) // 60
se = a % 60
print(ch, mi, se, sep = ":")
