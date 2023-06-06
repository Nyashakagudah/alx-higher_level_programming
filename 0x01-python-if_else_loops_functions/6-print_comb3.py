#!/usr/bin/python3
for b in range(0, 10):
    for c in range(1, 10):
        if b >= c:
            continue
        elif b == 8 and c == 9:
            print("{}{}".format(b, c))
        else:
            print("{}{}, ".format(b, c), end="")
