'''
Created on 23 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''
from cgitb import small
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

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def words_to_matrix(word_list):
    rows = len(word_list)
    cols = len(word_list[0])
    char_list = []
    for i in range(0, len(word_list), 1):
        char_list.append([char for char in word_list[i]])
    
    print("\n  ", end="")
    for i in range(0, cols, 1):
        print("{:4}".format(i), end="")
    print("")
    
    for i in range(0, rows, 1):
        print("{:2d}".format(i), end="")
        for j in range(0, cols, 1):
            print("{:>4}".format(char_list[i][j]), end="")
        print("")


word_list = ["cat", "dog", "big"]
print("Strings: ", word_list)
print("\nMatrix of characters:")
words_to_matrix(word_list)

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")

from random import randint

    
def print_matrix_num(matrix):
    print("  ", end="")
    
    for i in range(0, cols, 1):
        print("  {:5}".format(i), end="")
    print("")
    for i in range(0, rows, 1):
        print(" {}".format(i), end="")
        for j in range(0, cols, 1):
            print("  {:5}".format(matrix[i][j]), end="")
        print("")


def stats(matrix):
    smallest = 100
    largest = 0
    total = 0
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
            if matrix[i][j] > largest:
                largest = matrix[i][j]
            total += matrix[i][j]            
    if total > 0:
        average = total / (rows * cols)
    else:
        average = -1 * (abs(total) / (rows * cols))
    print("\nSmallest = {}\nLargest = {}\nTotal = {}\nAverage = {:.2f}".format(smallest, largest, total, average))


rows, cols, low, high = (3, 4, -10, 10)
# rows = int(input("Number of rows:"))
# cols = int(input("Number of columns:"))
# low = int(input("Low value:"))
# high = int(input("High value:"))
matrix = [[randint(low, high) for i in range(cols)] for j in range(rows)]
print_matrix_num(matrix)
stats(matrix)
'''
# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")
