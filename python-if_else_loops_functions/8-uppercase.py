#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 123:
            n = ord(i)
            n -= 32
            i = chr(n)
        print(i, end="")
    print("")
