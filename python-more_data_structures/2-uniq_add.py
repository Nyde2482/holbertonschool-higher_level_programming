#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    return sum(new_list)
