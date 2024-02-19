#!/usr/bin/bash
"""
a function that print the last digit on a number 

args:
    number:the inpu value
function:
    print_last_digit: takes number as argument 
    and returns the last digit
"""


def print_last_digit(number):
    last_digit = number % 10
    print("{}".format(last_digit), end(""))
