#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    args = sys.argv
    args_len = len(args) - 1

    op = str(args[2])
    if args_len == 3:
        message = "{} {} {} = {}"
        a = int(args[1])
        b = int(args[3])

        # checking for operator
        if args[2] == '+':
            print(message.format(a, op, b, calc.add(a, b)))
        elif args[2] == '-':
            print(message.format(a, op, b, calc.sub(a, b)))
        elif ord(args[2]) == 42:
            print(message.format(a, op, b, calc.mul(a, b)))
        elif ord(args[2]) == 47:
            print(message.format(a, op, b, calc.div(a, b)))
        sys.exit(0)
    
    elif args_len != 3:
        message = "Usage: ./100-my_calculator.py <a> <operator> <b>"
        print("{}".format(message))
        sys.exit(1)

    elif op != '+' and op != '-' and op != '*' and op != '/': 
        message = "Unknown operator. Available operators: +, -, * and /"
        print("{}".format(message))
        sys.exit(1)


