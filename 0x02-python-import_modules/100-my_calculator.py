#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = argv[1]
    op = argv[2]
    b = argv[3]
    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:s} {:s} {:s} = ".format(a, op, b), end='')
    if op == '+':
        print("{:d}".format(add(int(a),int(b))))
    if op == '-':
        print("{:d}".format(sub(int(a),int(b))))
    if op == '*':
        print("{:d}".format(mul(int(a),int(b))))
    if op == '/': 
        print("{:d}".format(div(int(a),int(b))))
