'''
Created on 02 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
import re


def file_head(fh, n):
    f = open(fh).read()
    my_list = re.split("\n", f)
    print("my_list", my_list)
    print("n", n)

    
fh = "wilde.txt"
open(fh, "r")
n = 0
file_head(fh, n)
