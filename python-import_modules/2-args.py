#!/usr/bin/python3
import sys


def main():
    total = len(sys.argv) - 1

    if total == 0:
        print("0 argument.")
    elif total == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(total))
        n = 1
        for i in sys.argv[1:]:
            print("{}: {}".format(n, i))
            n += 1


if __name__ == "__main__":
    main()
