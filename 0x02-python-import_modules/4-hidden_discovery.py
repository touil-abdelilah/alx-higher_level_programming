#!/usr/bin/python3
import dis
import types

def print_names(module):
    bytecode = module.__code__.co_code
    instructions = dis.get_instructions(bytecode)
    names = set()
    for instruction in instructions:
        if instruction.opname == 'LOAD_CONST':
            const = module.__code__.co_consts[instruction.arg]
            if isinstance(const, str) and not const.startswith('__'):
                names.add(const)

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()
        module = types.CodeType(
            0, 0, 0, 0, 67, code, (), (), (), '', '', 0, b'')
        print_names(types.ModuleType(module))
