'''
Created on 2019 M05 9
__updated__ = '2019-05-09'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
''' '''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
PENNYWEIGHT_TO_GRAM = 1.5552

start = int(input("Start: "))
limit = int(input("Limit: "))
inc = int(input("Increment: "))
grams = 0
print("\nPennyweight     Grams\n" + 11 * "-" + " " + 9 * "-")

for i in range(start, limit + 1, inc):
    grams = i * PENNYWEIGHT_TO_GRAM
    print("{:>11}  {:>8.4f}".format(i, grams))
'''
# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
width = int(input("Width of diamond: "))
character = input("Printing character: ")

for i in range(0, width, 1):
    print((width - i) * " " + i * "{}".format(character) + (i - 1) * "{}".format(character))
for i in range(width, 0, -1):
    print((width - i) * " " + i * "{}".format(character) + (i - 1) * "{}".format(character))
