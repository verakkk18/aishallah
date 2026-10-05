#!/usr/bin/python3
import sys
a = (sys.argv[1])
b = a[::-1]

c = b.translate(str.maketrans("TACG", "ATGC"))
print("комплементарная -", c)

r = c.replace("T", "U")
print("РНК -", r)

p=a.find("ATG")
print(p)
