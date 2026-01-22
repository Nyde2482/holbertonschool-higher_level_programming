#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for find in my_list:
        if find == search:
            new_list.append(replace)
        else:
            new_list.append(find)
    return new_list
