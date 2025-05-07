#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    if len(argv) != 4:
        print(len(argv))
        print("Usage: ./100-my_calculator.py a operator b")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    match op:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = float(div(a, b))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    main()
