#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    last = number % 10
    last = last * -1
else:
    last = number % 10

if last < 6 and last != 0:
    number = number * -1
    print("Last digit of {:d} is {:d} and is less than 6 and not 0\n".format(number, last))
elif last == 0:
    print("Last digit of {:d} is {:d} and is 0\n".format(number, last))
else:
    print("Last digit of {:d} is {:d} and is greater than 5\n".format(number, last))
