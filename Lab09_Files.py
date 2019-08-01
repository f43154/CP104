'''
Created on 20 06 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani

Completed in....far too long, took time off to commute for new job and eventually move to new home
'''
from shutil import copyfile
import re

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
    # print(my_nested_list)
    my_nested_list.append(fields)
    print("data appended to file")
    # print(my_nested_list)
    

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

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")


def count_frequency_value(fv, value):
    my_list = open(fv).read()
    my_list = [int(n) for n in my_list.split()]
    count = 0
    for i in range(0, len(my_list), 1):
        if my_list[i] == value:
            count += 1
    print("{} appears {} time(s)".format(value, count))


fv = "numbers.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' is open for reading".format(fv))
    value = int(input("Value to count: "))
    count_frequency_value(fv, value)

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")


def count_frequency_word(fv, word):
    my_list = open(fv).read()
    my_list = [n for n in my_list.split()]
    count = 0
    for i in range(0, len(my_list), 1):
        if word == my_list[i]:
            count += 1
    print("'{}' appears {} time(S)".format(word, count))


fv = "words.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' is open for reading".format(fv))
    word = input("Word to count: ")
    count_frequency_word(fv, word)

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")


def find_longest(fv):
    my_list = open(fv).read()
    my_list = [n for n in my_list.split()]
    word = ""
    for i in range(0, len(my_list), 1):
        if len(word) <= len(my_list[i]):
            word = my_list[i]
    print("'{}' is the last longest word".format(word))


fv = "words.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' is open for reading".format(fv))
    find_longest(fv)

# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")


def find_shortest(fv):
    my_list = open(fv).read()
    my_list = [n for n in my_list.split()]
    word = my_list[0]
    for i in range(len(my_list) - 1, -1, -1):
        if len(word) >= len(my_list[i]):
            word = my_list[i]
    print("'{}' is the first shortest word".format(word))


fv = "words.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' is open for reading".format(fv))
    find_shortest(fv)

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")


def delete_line(fv, n):
    my_list = open(fv).read()
    my_list = [n for n in my_list.split()]
    print("Line {} deleted:".format(n))
    print(my_list[n])
    my_list.pop(n)


fv = "words.txt"
f = open(fv, "r+")
if not f.closed:
    print("file '{}' is open for reading".format(fv))
    n = int(input("Enter line number to delete: "))
    delete_line(fv, n)

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")


def file_copy(fv_1, fv_2):
    copyfile(fv_1, fv_2)
    print("Copying '{}' to '{}'".format(fv_1, fv_2))


fv_1 = "words.txt"
fv_2 = "new_words.txt"
open(fv_2, "w+")
file_copy(fv_1, fv_2)

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")


def file_copy_n(fv_1, fv_2, n):
    fv_1_list = open(fv_1).read()
    fv_1_list = [n for n in fv_1_list.split()]
    fv_2_list = open(fv_2).read()
    fv_2_list = [n for n in fv_2_list.split()]
    fv_2_list.append(fv_1_list[0:n])


fv_1 = "words.txt"
fv_2 = "new_words.txt"
open(fv_2, "w+")
n = int(input("Number of lines to copy: "))
file_copy_n(fv_1, fv_2, n)
