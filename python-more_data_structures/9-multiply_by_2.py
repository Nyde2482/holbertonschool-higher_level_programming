#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        if isinstance(value, int):
            new_dict[key] = value * 2
    return new_dict
