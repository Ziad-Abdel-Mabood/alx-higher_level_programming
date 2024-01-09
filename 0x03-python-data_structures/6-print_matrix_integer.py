#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in range(len(row)):
            print("{:d}".format(row[x]), end='')
            if x < (len(row)-1):
                print(" ", end='')
        print("")
