#!/usr/bin/env python3
import argparse
from calculator import add, subtract, multiply, divide


def calculate(a, b, operation):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        try:
            return divide(a, b)
        except ValueError as e:
            return str(e)
    else:
        return "Unknown operation"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("a")
    parser.add_argument("b")
    args = parser.parse_args()
    result = calculate(float(args.a), float(args.b), args.operation)

    print(result)


if __name__ == "__main__":
    main()
