#!/usr/bin/python3
import hidden_4


def main():
    d_name = dir(hidden_4)

    for i in d_name:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    main()
