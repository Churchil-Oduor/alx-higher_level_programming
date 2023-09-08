#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1

    a = 10
    b = 5

    my_sum = calculator_1.add(a, b)
    sub = calculator_1.sub(a, b)
    div = calculator_1.div(a, b)
    mul = calculator_1.mul(a, b)

    print("{} + {} = {}".format(a, b, my_sum))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
