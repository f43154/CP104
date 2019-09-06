'''
Created on 23 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''
from cgitb import small
from random import randint
from random import uniform
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


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

# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")


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


def find_word_diagonal(matrix, word):
    # Turn strings into a list where with all characters separated
    print()
    new_matrix = []
    for i in range(0, len(matrix), 1):
        new_matrix += list(matrix[i])
    
    # Reassemble the list with the new words diagonally BOTTOM LEFT TO TOP RIGHT
    bottom_left = []
    left_reconstructed = new_matrix[6] + new_matrix[4] + new_matrix[2]
    bottom_left.append(left_reconstructed)
    bottom_left = list(bottom_left[0])
    
    # Reassemble the list with the new words diagonally TOP LEFT TO BOTTOM RIGHT
    top_left = []
    right_reconstructed = new_matrix[0] + new_matrix[4] + new_matrix[8]
    top_left.append(right_reconstructed)
    top_left = list(top_left[0])
    
    # Search and return true/false for diagonal
    bottom_left_diagonal = 0
    top_left_diagonal = 0
    for i in range(0, 3, 1):
        if top_left[i] == word[i]:
            top_left_diagonal += 1
        if bottom_left[i] == word[i]:
            bottom_left_diagonal += 1
            
    if top_left_diagonal == 3:
        print("The word '{}' is found on the diagonal (starting from top left).".format(word))
    elif bottom_left_diagonal == 3:
        print("The word '{}' is found on the diagonal (starting from bottom left).".format(word))
    else:
        print("The word '{}' is not found on the diagonal.".format(word))


matrix = ["cat", "dog", "big"]
rows = len(matrix)
cols = len(matrix[0])
print_matrix_char(matrix)
word = "bot"
find_word_diagonal(matrix, word)

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")

    
def print_matrix_num(matrix):
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


def scalar_multiply(matrix, num):
    new_list = []
    for i in range(0, len(matrix), 1):
        for j in range(0, len(matrix[0]), 1):            
            new_num = matrix[i][j] * num
            new_list.append(new_num)
    
    # Turn list into a 2D array using a list comprehension
    new_matrix = [new_list[i:i + cols] for i in range(0, len(new_list), cols)]   
    return new_matrix


rows, cols, low, high = (4, 3, -10, 10)
matrix = [[randint(low, high) for i in range(cols)] for j in range(rows)]
print_matrix_num(matrix)
num = int(input("\nEnter number:"))
print_matrix_num(scalar_multiply(matrix, num))

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")


def print_matrix_num(matrix):
    print("")
    print("Original matrix:")
    print("  ", end="")
    
    for i in range(0, cols, 1):
        print("  {:4.0f}".format(i), end="")
    print("")
    for i in range(0, rows, 1):
        print(" {}".format(i), end="")
        for j in range(0, cols, 1):
            print("  {:4.0f}".format(matrix[i][j]), end="")
        print("")


def matrix_transpose(a):    
    new_matrix = [[row[i] for row in matrix] for i in range(cols)]
    print("")
    print("Transposed matrix:")
    print("  ", end="")
    
    for i in range(0, rows, 1):
        print("  {:4.0f}".format(i), end="")
    print("")
    for i in range(0, cols, 1):
        print(" {}".format(i), end="")
        for j in range(0, rows, 1):
            print("  {:4.0f}".format(new_matrix[i][j]), end="")
        print("")

        
rows, cols, low, high = (4, 3, -10, 10)
matrix = [[randint(low, high) for i in range(cols)] for j in range(rows)]
print_matrix_num(matrix)

# Turn 2D array back into list
a = []
for i in range(0, len(matrix), 1):
    a += list(matrix[i])

matrix_transpose(a)

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")


def list_to_2darray(word_list):
    rows = len(word_list)
    cols = len(word_list[0])
    char_list = []
    for i in range(0, len(word_list), 1):
        char_list.append([char for char in word_list[i]])
    return char_list


def print_2darray(word_list, char_list):
    rows = len(word_list)
    cols = len(word_list[0])
    
    print("  ", end="")
    for i in range(0, cols, 1):
        print("{:4}".format(i), end="")
    print("")
    
    for i in range(0, rows, 1):
        print("{:2d}".format(i), end="")
        for j in range(0, cols, 1):
            print("{:>4}".format(char_list[i][j]), end="")
        print("")    


def matrix_equal(matrix1, matrix2):
    total = len(matrix1) * len(matrix1[0]) 
    counter = 0
    for i in range(0, len(matrix1), 1):
        for j in range(0, len(matrix1[0]), 1):
            if matrix1[i][j] == matrix2[i][j]:
                counter += 1
    if counter == total:
        return True
    else:
        return False


print("First matrix:")
word_list1 = ["cat", "dog", "big"]
word_list2 = ["cat", "dog", "big"]
print_2darray(word_list1, list_to_2darray(word_list1))
print("\nSecond matrix:")
print_2darray(word_list2, list_to_2darray(word_list2))
print("\nEqual matrices:", matrix_equal(list_to_2darray(word_list1), list_to_2darray(word_list2)))
