#!/usr/bin/python3
s = input()
o = ""
for c in s:
    if c == "A":
        o += "T"
    elif c == "T":
        o += "A"
    elif c == "C":
        o  += "G"
    elif c == "G":
        o += "C"
print (o[::-1])
