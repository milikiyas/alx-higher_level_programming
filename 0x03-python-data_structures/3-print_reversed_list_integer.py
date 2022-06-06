#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    lists = []
    for i in my_list:
        lists.append(i)
        print('{}'.format(i))
