#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list
    a.reverse()
    lists = []
    for i in a:
        lists.append(i)
        print('{}'.format(i))
