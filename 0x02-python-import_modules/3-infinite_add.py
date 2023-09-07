#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    elements = sys.argv
    count = len(elements)

    add = 0
    if count == 1:
        print("{}".format(0))
    else:
        for i in range(1, count):
            num = elements[i]
            num = int(num)
            add += num
        print("{}".format(add))
