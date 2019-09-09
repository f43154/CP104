'''
Created on 09 09 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def binary_search(values, key):
    if values[int(len(values) / 2)] > key:
        print("if bigger", int(len(values) / 2))
        if values[int(len(values) - (len(values) / 2))] > key:
            print("if bigger, big sublist, bigger", int(len(values) - (len(values) / 2)))
        if values[int(len(values) - (len(values) / 2))] <= key:
            print("if bigger, big sublist, smaller", int(len(values) - (len(values) / 2)))
    elif values[int(len(values) / 2)] <= key:
        print("if smaller equal", int(len(values) / 2))
        if values[int((len(values) / 2) / 2)] > key:
            print("if smaller equal, small sublist, bigger", int((len(values) / 2) / 2))
        if values[int((len(values) / 2) / 2)] <= key:
            print("if smaller equal, small sublist, smaller", int((len(values) / 2) / 2))
    else:
        print("else")

    
values = [2, 5, 5, 5, 5, 5, 5, 8]
print("Search: {} ".format(values), end="")
key = int(input("for "))
binary_search(values, key)
