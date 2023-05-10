#!/usr/bin/python3

def print_last_digit(number):
    l_digit = 0

    if number < 0:
        number *= -1

    l_digit = number % 10

    print(l_digit, end="")

    return l_digit
