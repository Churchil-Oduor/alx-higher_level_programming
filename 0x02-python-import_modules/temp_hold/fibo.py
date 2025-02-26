#!/usr/bin/python3

def add(a):
    print(f"{a + 10}")


if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]))
