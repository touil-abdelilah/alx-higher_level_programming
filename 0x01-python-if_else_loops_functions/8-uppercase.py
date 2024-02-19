#!/usr/bin/python3


def uppercase(str):
    for c in str:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            upper = ord(c) - 32
            print("{}".format(chr(upper)), end="")
    print("\n")
