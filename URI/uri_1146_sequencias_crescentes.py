#!/usr/bin/env python3

while True:
    y,z = str(),str()
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(1,x+1):
            z = str(i)
            y += z + " "
    print(y.rstrip())
