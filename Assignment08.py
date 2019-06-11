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
    subset = []
    for i in range(0, len(string), 1):
        j = i + 1
        while j < len(string):
            subset.append(string[i] + string[j])
            j += 1
    print("Subsets: ", subset)

    
string = input("String: ")
two_element_subset(string)
'''
# # # # # TASK 4 # # # # #
from random import randint

print("\n# # # # # TASK 4 # # # # #")

subjects = ["David", "Tasmin", "Tristan", "Lori", "Kate", "Li-Meng"]
print(subjects)

for i in range(0, len(subjects), 1):
    drugs = []
    placebos = []
    random = randint(0, 1)
    if random == 1:
        drugs.append(subjects[i])
        print("Drugs", drugs)
    else:
        placebos.append(subjects[i])
        print("Placebos ", placebos)

print("\n")
print("Placebos: {}".format(placebos))
print("Drugs: {}".format(drugs))
