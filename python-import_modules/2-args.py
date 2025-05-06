#!/usr/bin/python3
from sys import argv


def main():
    n = 1
    total = len(argv) - 1

    if total == 0:
        print("0 arguments.")

    elif total == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))

    else:
        print("{} arguments:".format(total))
        for i in argv[1:]:
            print("{}: {}".format(n, i))
            n += 1


if __name__ == "__main__":
    main()
