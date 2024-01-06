#!/usr/bin/python3
import dis

# Load the bytecode from the file
with open('hidden_4.pyc', 'rb') as file:
    code = file.read()

# Disassemble the bytecode
instructions = dis.get_instructions(code)

# Iterate through the instructions and find the names
names = set()
for instr in instructions:
    if instr.opname == 'LOAD_NAME' and not instr.argrepr.startswith('__'):
        names.add(instr.argrepr)

# Print the names in alphabetical order
for name in sorted(names):
    print(name)


if __name__ == "__main__":
    file_path = 'hidden_4.pyc'
    extract_names(file_path)
