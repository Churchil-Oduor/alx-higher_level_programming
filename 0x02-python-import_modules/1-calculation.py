#!/usr/bin/python3
if __name__ == '__main__':
    import calculator as calc

    a = 10
    b = 5

    my_sum = calc.add(a, b)
    sub = calc.sub(a, b)
    div = calc.div(a, b)
    mul = calc.mul(a, b)

    print("{} + {} = {}".format(a, b, my_sum))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
