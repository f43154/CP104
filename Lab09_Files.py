'''
Created on 20 06 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani

Completed Task 1 in....far too long, took time off to commute for new job and eventually move to new home
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def customer_records(fv, n):
    my_list = open(fv).read()
    my_list = re.split(",|\n", my_list)
    my_nested_list = []
    start = 0
    end = 5
    num_lines = int(len(my_list) / 5)
    i = 0
    while i < num_lines:
        my_nested_list.append(my_list[start:end])
        start += 5
        end += 5
        i += 1
    if n >= 5:
        print("[]")
    else:
        print(my_nested_list[n])


import re
fv = "customers.txt"
print("Find record n")
n = int(input("Find a record number:  "))
customer_records(fv, n)
