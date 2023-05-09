#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negative_flag = 0

if number < 0:
    number = number * -1
    negative_flag = 1

_digit = number % 10

if negative_flag == 1:
    _digit *= -1
    number *= -1

if _digit > 5:
    print(f"Last digit of {number} is {_digit} and is greater than 5")

elif _digit < 6 and _digit != 0:
    print(f"Last digit of {number} is {_digit} and is less than 6 and not 0")

else:
    print(f"Last digit of {number} is {_digit} and is 0")
