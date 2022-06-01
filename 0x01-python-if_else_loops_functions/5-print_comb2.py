#!/usr/bin/python3
k = 0
while k <= 99:
   if k <= 98:
    print('{:02}'.format(k), end=", ")
    k += 1
   else:
    print('{:02}'.format(k))
    k += 1
