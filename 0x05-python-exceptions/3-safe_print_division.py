#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b! = 0:
            result = a/b
        else:
            result = None
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
        return result
