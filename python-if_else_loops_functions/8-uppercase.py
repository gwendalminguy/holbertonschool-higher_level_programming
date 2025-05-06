#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if 97 <= n <= 123:
            n -= 32
        print("{:c}".format(n), end="")
    print("")
