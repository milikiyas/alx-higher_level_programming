#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = abs(number) % 10
short = 'Last digit of'
if number < 0:
    number1 *= -1
if number1 > 5:
    print(short, '{} is {} and is greater than 5'.format(number, number1))
elif number1 == 0:
    print(short, '{} is {} and is 0'.format(number, number1))
elif number1 < 6:
    short_1 = "Last digit of {} is {} and is less than 6 and not 0"
    print(short_1.format(number, number1))
