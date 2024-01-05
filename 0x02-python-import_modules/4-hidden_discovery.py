#!/usr/bin/python
import dis
import types

def print_names(module):
    bytecode = module.__code__
    names = []
    for instruction in dis.get_instructions(bytecode):
        if 'LOAD_NAME' in instruction.opname and not instruction.argrepr.startswith(('<', '__')):
            names.append(instruction.argrepr)

    names = sorted(set(names))
    for name in names:
        print(name)

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()
        module = types.CodeType(
            0, 0, 0, 0, 67, code, (), (), (), '', '', 0, b'')
        print_names(types.ModuleType(module))
