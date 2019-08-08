'''
Created on 02 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani

Completed Task 1 and 2 in 30 mins
'''
import re

from pip._vendor.html5lib._ihatexml import letter

'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
import re


def file_head(fh, n):
    f = open(fh).read()
    my_list = re.split("\n", f)
    my_list = [quotes for quotes in my_list if quotes.strip()]
    i = 0
    while i < (n + 1):
        print(my_list[i])
        print()
        i += 1

    
fh = "wilde.txt"
open(fh, "r")
print("Enter input file name:", fh)
n = int(input("Enter n:"))
print()
file_head(fh, n)

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")

import re


def number_lines(fh_in, fh_out):
    f = open(fh_in).read()
    f_out = open(fh_out, "a+")
    my_list = re.split("\n", f)
    my_list = [quotes for quotes in my_list if quotes.strip()]
    for i in range(0, len(my_list), 1):
        f_out.write("[%d] %s\n" % (i, my_list[i]))

    
fh_in = "wilde.txt"
fh_out = "wilde_numbered.txt"
open(fh_in, "r")
print("Enter input file name:", fh_in)
print("Enter output file name:", fh_out)
number_lines(fh_in, fh_out)

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")

import re


def get_addresses(fh):
    f = open(fh).read()
    my_list = re.split("[-:]|\n", f)
    my_list = [spaces for spaces in my_list if spaces.strip()]
    my_nested_list = []
    start = 0
    end = 4
    i = 0
    while i < (len(my_list) / 4):
        my_nested_list.append(my_list[start:end])
        start += 4
        end += 4
        i += 1
    for j in range(0, len(my_nested_list), 1):
        print(my_nested_list[j])


fh = "addresses.txt"
print("Enter address file name:", fh)
print()
get_addresses(fh)
'''
# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")


def merge_letters(fh_letter, fh_addresses, fh_merged):
    # compile and clean addresses
    f = open(fh_addresses).read()
    my_list = re.split("[-:]|\n", f)
    my_list = [spaces for spaces in my_list if spaces.strip()]
    nested_address_list = []
    start = 0
    end = 4
    i = 0
    while i < (len(my_list) / 4):
        nested_address_list.append(my_list[start:end])
        start += 4
        end += 4
        i += 1
        
    # import letter template
    f_letter = open(fh_letter, "r")
    letter_template = f_letter.read()

    # merge addresses into letter template
    letter_template.replace("[forename]", nested_address_list[0][0])
    print(letter_template)
    print(nested_address_list[0][0])


fh_letter = "letter.txt"
fh_addresses = "addresses.txt"
fh_merged = "merged_letters.txt"
merge_letters(fh_letter, fh_addresses, fh_merged)
