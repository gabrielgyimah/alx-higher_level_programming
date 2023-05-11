#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    add_ans = add(a, b)
    sub_ans = sub(a, b)
    mul_ans = mul(a, b)
    div_ans = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_ans))
    print("{:d} - {:d} = {:d}".format(a, b, sub_ans))
    print("{:d} * {:d} = {:d}".format(a, b, mul_ans))
    print("{:d} / {:d} = {:d}".format(a, b, div_ans))


if __name__ == "__main__":
    main()
