#!/usr/bin/python3
from sys import argv


def main():
    result = 0

    for i in range(1, len(argv)):
        result += int(argv[i])

    print(result)


if __name__ == "__main__":
    main()
