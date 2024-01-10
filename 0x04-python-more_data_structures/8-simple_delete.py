#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Use try-except to handle the case where the key doesn't exist
    try:
        del a_dictionary[key]
    except KeyError:
        pass

    return a_dictionary

# Function to print the dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
