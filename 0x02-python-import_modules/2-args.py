#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
        return

    if argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[1]))
        return

    print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
