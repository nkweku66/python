#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldigit = number % -10
else:
    ldigit = number % 10
message = f"Last digit of {number:d} is {ldigit:d} and is"
if ldigit > 5:
    print(message+" greater than 5")
elif ldigit < 6 and ldigit != 0:
    print(message+" less than 6 and not 0")
else:
    print(message+" 0")
