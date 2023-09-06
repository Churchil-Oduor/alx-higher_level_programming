#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

msg1 = ("Last digit of {0} is {1:.0f} and is greater than 5")
msg2 = ("Last digit of {0} is {1:.0f} and is less than 6 and not 0")
msg3 = ("Last digit of {0} is {1:.0f} less than 6 and not 0")
if number >= 0:
    # the number is opositive
    last_digit = number % 10
    if last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number, last_digit))
    elif last_digit > 5:
        print(msg1.format(number, last_digit))
    else:
        print(msg2.format(number, last_digit))
else:
    number *= -1
    last_digit = number % 10
    print(msg3.format(number * -1, last_digit * -1))
