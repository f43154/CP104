'''
Created on 23 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
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
