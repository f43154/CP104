'''
Created on 02 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani

Completed Task 1 and 2 in 30 mins
'''
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
'''
# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
