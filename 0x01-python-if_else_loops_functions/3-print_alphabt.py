#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    if chr(i) in ['q', 'e']:
        pass
    else:
        print("{}".format(chr(i)), end='')
