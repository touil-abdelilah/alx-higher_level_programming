#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except KeyError:
        pass

    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
