#!/usr/bin/python3
a, b = int(input()), int(input())

a1s = id(a)
b1s = id(b)

a, b = b, a

a1 = id(a)
a2 = id(b)

print("a =", a, "b =", b, "id до:", a1s, b1s, "id после:", a1, a2)

c, d = int(input()), int(input()) #1000, 2000

c1 = id(c)
d1 = id(d)

j = c                             #1000, 1000
c = d
d = j

c2 = id(c)
d2 = id(d)
print("c=", c, "d =", d, "id до:", c1, d1, "id после:", c2, d2)


