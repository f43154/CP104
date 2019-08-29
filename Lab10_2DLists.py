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

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")

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
                smallest_position = [i, j]
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                largest_position = [i, j]
            total += matrix[i][j]            
    print("\nSmallest position: {}\nSmallest value: {}\nLargest position: {}\nLargest value: {}".format(smallest_position, smallest, largest_position, largest))


rows, cols, low, high = (3, 4, -10, 10)
print("Number of rows: {}\nNumber of columns: {}\nLow value: {}\nHigh value: {}\n".format(rows, cols, low, high))
# rows = int(input("Number of rows:"))
# cols = int(input("Number of columns:"))
# low = int(input("Low value:"))
# high = int(input("High value:"))
matrix = [[randint(low, high) for i in range(cols)] for j in range(rows)]
print_matrix_num(matrix)
stats(matrix)

# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")

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


def find_less(matrix, n):
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if matrix[i][j] < n:
                n = matrix[i][j]
                position = [i, j]
    print("\nPosition: {}\nValue: {}".format(position, n))


rows, cols, low, high, n = (3, 4, -10, 10, 3)
print("Number of rows: {}\nNumber of columns: {}\nLow value: {}\nHigh value: {}\nTarget value: {}\n".format(rows, cols, low, high, n))
# rows = int(input("Number of rows:"))
# cols = int(input("Number of columns:"))
# low = int(input("Low value:"))
# high = int(input("High value:"))
matrix = [[randint(low, high) for i in range(cols)] for j in range(rows)]
print_matrix_num(matrix)
find_less(matrix, n)

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")

from random import randint


def generate_matrix_char(rows, cols):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = [char for char in alphabet]
    matrix = [[alphabet[randint(0, 25)] for i in range(cols)] for j in range(rows)]
    return matrix


def print_matrix_char(matrix):
    print("\n  ", end="")
    for i in range(0, cols, 1):
        print("{:4}".format(i), end="")
    print("")
    
    for i in range(0, rows, 1):
        print("{:2d}".format(i), end="")
        for j in range(0, cols, 1):
            print("{:>4}".format(matrix[i][j]), end="")
        print("")


def count_frequency(matrix, c):
    count = 0
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if matrix[i][j] == c:
                count += 1
    print("\nEnter the character to search for: {}\nCharacter {} appears {} times in matrix.".format(c, c, count))
    

rows, cols, c = (5, 4, "c")
# rows = int(input("Number of rows:"))
# cols = int(input("Number of columns:"))
matrix = generate_matrix_char(rows, cols)
print_matrix_char(matrix)
count_frequency(matrix, c)

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")


def print_matrix_char(strings):
    print("\n  ", end="")
    for i in range(0, cols, 1):
        print("{:4}".format(i), end="")
    print("")
    
    for i in range(0, rows, 1):
        print("{:2d}".format(i), end="")
        for j in range(0, cols, 1):
            print("{:>4}".format(matrix[i][j]), end="")
        print("")


def find_word_horizontal(matrix, word):
    position = ""
    for i in range(0, rows, 1):
        if matrix[i] == word:
            position = i 
    print("\nThe word to search for is: {}\n\nThe word is found in rows [{}]".format(word, position))
    

matrix = ["cat", "dog", "big"]
rows = len(matrix)
cols = len(matrix[0])
print_matrix_char(matrix)
word = "dog"
find_word_horizontal(matrix, word)

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")


def print_matrix_char(strings):
    print("\n  ", end="")
    for i in range(0, cols, 1):
        print("{:4}".format(i), end="")
    print("")
    
    for i in range(0, rows, 1):
        print("{:2d}".format(i), end="")
        for j in range(0, cols, 1):
            print("{:>4}".format(matrix[i][j]), end="")
        print("")


def find_word_vertical(matrix, word):
    # Turn strings into a list where with all characters separated
    new_matrix = []
    for i in range(0, len(matrix), 1):
        new_matrix += list(matrix[i])
    
    # Reassemble the list with the new words
    column_list = []
    word_reconstructed = []
    i = 0
    while i < (len(new_matrix) / len(matrix[0])):
        word_reconstructed = new_matrix[i] + new_matrix[i + 3] + new_matrix[i + 6]
        column_list.append(word_reconstructed)
        i += 1
    
    # Search and return position
    position = ""
    for i in range(0, rows, 1):
        if column_list[i] == word:
            position = i 
    print("\nThe word to search for is: {}\n\nThe word is found in rows [{}]".format(word, position))
    

matrix = ["cdb", "aoi", "tgg"]
rows = len(matrix)
cols = len(matrix[0])
print_matrix_char(matrix)
word = "big"
find_word_vertical(matrix, word)
'''
# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")
