#!/usr/bin/python3

import sys

m = float(sys.argv[1])
p = float(sys.argv[2])
y = float(sys.argv[3])

s = m * ( 1 + p/100) ** y

print(round(s, 2))
