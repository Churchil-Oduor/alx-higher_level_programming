#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    elements = sys.argv

    if num == 0:
        print("{} arguments.".format(num))

    elif num == 1:

        print("{} argument:".format(num))
        for i in range(1, num + 1):
            print("{}: {}".format(i, elements[i]))
    else:

        print("{} arguments:".format(num))
        for i in range(1, num + 1):
            print("{}: {}".format(i, elements[i]))
