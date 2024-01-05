#!/usr/bin/python3
import types
import sys

def extract_names(file_path):
    with open(file_path, 'rb') as file:
        magic_number = file.read(4)
        mod_time = file.read(4)
        code_obj = types.CodeType.from_traceback(file.read())

        names = sorted(set(code_obj.co_names))
        for name in names:
            if not name.startswith('__'):
                print(name)

if __name__ == "__main__":
    file_path = 'hidden_4.pyc'
    extract_names(file_path)
