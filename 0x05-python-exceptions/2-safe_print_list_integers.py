#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    def safe_print_list_integers(my_list=[], x=0):
    index = hello = 0
    while True:
        try:
            if index < x:
               print('{:d}'.format(my_list[index]), end='')
               index += 1
               hello += 1
            else:
                print()
                return hello
        except (TypeError, ValueError):
            index += 1
