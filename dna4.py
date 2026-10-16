#!/usr/bin/python3
a = input()
gc = 0

for c in a:
    if c == "G" or c == "C":
        gc +=1
print(gc / len(a) * 100)
