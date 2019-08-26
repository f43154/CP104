'''
Created on 23 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")

from random import randint
from random import uniform


def generate_matrix_num(rows, cols, low, high, value_type):
    if value_type == "int":
        array = [[randint(low, high) for i in range(cols)] for j in range(rows)]
    elif value_type == "float":
        array = [[uniform(low, high) for i in range(cols)] for j in range(rows)]
    else:
        array = [["*" for i in range(cols)] for j in range(rows)]
    print(array)


rows = int(input("Number of rows:"))
cols = int(input("Number of columns:"))
low = int(input("Low value:"))
high = int(input("High value:"))
value_type = input("Type of value:")
generate_matrix_num(rows, cols, low, high, value_type)

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
from random import randint


def generate_matrix_char(rows, cols):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = [char for char in alphabet]
    array = [[alphabet[randint(0, 25)] for i in range(cols)] for j in range(rows)]
    print(array)


rows = int(input("Number of rows:"))
cols = int(input("Number of columns:"))
print("\nMatrix of characters:\n")
generate_matrix_char(rows, cols)

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")

from random import randint
from random import uniform


def generate_matrix_num(rows, cols, low, high, value_type):
    if value_type == "int":
        matrix = [[randint(low, high) for i in range(cols)] for j in range(rows)]
    elif value_type == "float":
        matrix = [[uniform(low, high) for i in range(cols)] for j in range(rows)]
    else:
        matrix = [["*" for i in range(cols)] for j in range(rows)]
    return matrix

    
def print_matrix_num(matrix, value_type):
    if value_type == "int":
        print("")
        print("  ", end="")
        
        for i in range(0, cols, 1):
            print("  {:4.0f}".format(i), end="")
        print("")
        for i in range(0, rows, 1):
            print(" {}".format(i), end="")
            for j in range(0, cols, 1):
                print("  {:4.0f}".format(matrix[i][j]), end="")
            print("")
    if value_type == "float":
        print("  ", end="")
        
        for i in range(0, cols, 1):
            print("  {:5.0f}".format(i), end="")
        print("")
        for i in range(0, rows, 1):
            print(" {}".format(i), end="")
            for j in range(0, cols, 1):
                print("  {:5.2f}".format(matrix[i][j]), end="")
            print("")
    else:
        print("Matrix not printed because improper value-type")


rows = int(input("Number of rows:"))
cols = int(input("Number of columns:"))
low = int(input("Low value:"))
high = int(input("High value:"))
value_type = input("Type of value:")
print_matrix_num(generate_matrix_num(rows, cols, low, high, value_type), value_type)

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
from random import randint


def generate_matrix_char(rows, cols):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = [char for char in alphabet]
    matrix = [[alphabet[randint(0, 25)] for i in range(cols)] for j in range(rows)]
    return matrix


def print_matrix_char(matrix):
    print("\n    ", end="")
    for i in range(0, cols, 1):
        print("{:4}".format(i), end="")
    print("")
    
    for i in range(0, rows, 1):
        print("{:4d}".format(i), end="")
        for j in range(0, cols, 1):
            print("{:>4}".format(matrix[i][j]), end="")
        print("")


rows = int(input("Number of rows:"))
cols = int(input("Number of columns:"))
print_matrix_char(generate_matrix_char(rows, cols))
'''
# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
