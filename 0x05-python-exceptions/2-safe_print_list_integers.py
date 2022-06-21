#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = am = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                am += 1
            else:
                print()
                return am
        except ValueError:
            index += 1
