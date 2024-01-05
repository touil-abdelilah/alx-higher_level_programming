#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        magic = file.read(4)
        mod_date = file.read(4)
        code_obj = marshal.load(file)

        names = [name for name in code_obj.co_names if not name.startswith('__')]
        names.sort()

        for name in names:
            print(name)
