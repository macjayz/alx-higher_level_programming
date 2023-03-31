#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_num = number % -10
else:
    new_num = number % 10
if new_num > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, new_num))
elif new_num < 6 && != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, new_num))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, new_num))
