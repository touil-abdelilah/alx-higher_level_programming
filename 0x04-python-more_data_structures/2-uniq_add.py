#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers and sum them up
    unique_sum = sum(set(my_list)) 
    return unique_sum
