'''
Created on 10 06 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")

from random import choices


def bag_to_set(bag):
    new_set = []
    for i in range(0, len(bag), 1):
        if bag[i] not in new_set:
            new_set.append(bag[i])
    return new_set


bag = choices(range(10), k=5)
print("Bag: ", bag)
print("Set: ", bag_to_set(bag))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")

from random import choices


def clean_list(values):
    new_values = []
    for i in range(0, len(values), 1):
        if values[i] not in new_values:
            new_values.append(values[i])    
    values = new_values
    return values


values = choices(range(5), k=10)
print("Values:\t", values)
print("Cleaned: ", clean_list(values))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def two_element_subset(string):
    i = 0
    while i < len(string):
        j = i + 1
        subsets = string[i] + string[j]
        i += 1
    print(subsets)

    
string = input("String: ")
two_element_subset(string)
'''
string = "AECG"
print(string[1])
