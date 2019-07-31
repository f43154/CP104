'''
Created on 20 06 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani

Completed Task 1 in....far too long, took time off to commute for new job and eventually move to new home
'''
from cgitb import small
from pickle import APPEND
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def customer_records(fv, n):
    # Import and separate the items by comma using re.split(",|\n",my_list)
    my_list = open(fv).read()
    my_list = re.split(",|\n", my_list)
    
    # Make a nested list from the imported customers.txt where everything is separated
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
    
    # To prevent Index Error
    if n >= 5:
        print("[]")
    else:
        print(my_nested_list[n])


import re
fv = "customers.txt"
print("Find record n")
n = int(input("Find a record number:  "))
customer_records(fv, n)

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")



def customer_by_id(fv, id_number):
    # Make list from customers.txt, separated by \n and ,
    my_list = open(fv).read()
    my_list = re.split(",|\n", my_list)
    
    # Make a nested list
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
        
    # To prevent Index Error and to print the ID and four remaining items following it
    if (id_number in my_list):
        my_index = my_list.index(id_number)
        print(my_list[my_index:my_index + 5])
    else:
        print("[]")

    
import re

fv = "customers.txt"
print("Find customer by id number")
id_number = input("Enter an ID: ")
if id_number.isdigit():
    customer_by_id(fv, id_number)
else:
    print("[]")

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def customer_by_id(fv):
    # Make list from customers.txt, separated by \n and ,
    my_list = open(fv).read()
    my_list = re.split(",|\n", my_list)
    
    # Make a nested list
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
    
    # Target balances within nested list
    i = 0
    largest_balance = 0
    while i < num_lines:
        if float(my_nested_list[i][3]) > float(largest_balance):
            largest_balance = my_nested_list[i][3]
            my_index = i
        i += 1
    print(my_nested_list[my_index])

    
import re

fv = "customers.txt"
print("FInd customer with largest balance:")
customer_by_id(fv)

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")


def customer_by_id(fv):
    # Make list from customers.txt, separated by \n and ,
    my_list = open(fv).read()
    my_list = re.split(",|\n", my_list)
    
    # Make a nested list
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
    
    # Find earliest sign-in
    i = 0
    my_index = 0
    earliest_signin = '9999-00-00'
    while i < num_lines:
        if my_nested_list[i][4] < earliest_signin:
            earliest_signin = my_nested_list[i][4]
            my_index = i
        i += 1
    print(my_nested_list[my_index])

    
import re

fv = "customers.txt"
print("Find customer with earliest sign-in:")
customer_by_id(fv)

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def customer_by_id(fv, fields):
    # Make list from customers.txt, separated by \n and ,
    my_list = open(fv).read()
    my_list = re.split(",|\n", my_list)
    
    # Make a nested list
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
    print(my_nested_list)
    my_nested_list.append(fields)
    print("data appended to file")
    print(my_nested_list)

    
import re

fv = "customers.txt"
fields = input("Data:")
customer_by_id(fv, fields)

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")


def number_stats(fv):
    my_list = open(fv).read()
    my_list = [int(n) for n in my_list.split()]
    total = 0
    smallest = 0
    largest = 0
    for i in range(0, len(my_list), 1):
        total += my_list[i]
        if my_list[i] < smallest:
            smallest = my_list[i]
        if my_list[i] > largest:
            largest = my_list[i]
    print("Smallest:", smallest)
    print("Largest:", largest)
    print("Total: {:.2f}".format(total))
    print("Average: {:.2f}".format(total / len(my_list)))


fv = "numbers.txt"
number_stats(fv)

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def append_max_num(fv):
    my_list = open(fv).read()
    my_list = [int(n) for n in my_list.split()]
    num = 0
    for i in range(0, len(my_list), 1):
        if my_list[i] > num:
            num = my_list[i]
    print("{} is appended".format(num))


fv = "numbers.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' open for reading and writing".format(fv))
    append_max_num(fv)

# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")


def append_increment(fv):
    my_list = open(fv).read()
    my_list = [int(n) for n in my_list.split()]
    num = 0
    for i in range(0, len(my_list), 1):
        if my_list[i] > num:
            num = my_list[i]
        my_list.append(num + 1)
    print("{} is appended".format(my_list[len(my_list) - 1]))


fv = "numbers.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' open for reading and writing".format(fv))
    append_increment(fv)
'''
# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")
