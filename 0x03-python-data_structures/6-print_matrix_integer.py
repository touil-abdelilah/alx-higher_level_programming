#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for  val in matrix:
        for nbr in val:
            print("{:d} ".format(nbr),end='')

        print('$')
