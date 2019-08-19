'''
Created on 02 08 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani

Completed Task 1 and 2 in 30 mins
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
from test.test_threading_local import target
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
    
    # merge addresses into letter template
    for i in range(0, len(nested_address_list), 1):
        replacements = {"[forename]":nested_address_list[i][0], "[surname]":nested_address_list[i][1], "[street]":nested_address_list[i][2], "[city]":nested_address_list[i][3]}
        lines = []
        with open(fh_letter) as infile:
            for line in infile:
                for src, target in replacements.items():
                    line = line.replace(src, target)
                lines.append(line)
        with open(fh_merged, "a") as outfile:
            for line in lines:
                outfile.write(line)


fh_letter = "letter.txt"
fh_addresses = "addresses.txt"
fh_merged = "merged_letters.txt"
merge_letters(fh_letter, fh_addresses, fh_merged)

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def student_info(students):
    f = open(fh).read()
    my_list = re.split("\n|\t", f)
    my_list = [spaces for spaces in my_list if spaces.strip()]
    nested_list = []
    start = 0
    end = 2
    i = 0
    while i < (len(my_list) / 2):
        nested_list.append(my_list[start:end])
        start += 2
        end += 2
        i += 1
    
    lowest = 100
    highest = 0
    total = 0
    
    for i in range(0, len(nested_list), 1):
        if int(nested_list[i][1]) > highest:
            highest = int(nested_list[i][0])
        if int(nested_list[i][1]) < lowest:
            lowest = int(nested_list[i][0])
        total += int(nested_list[i][1])
    
    average = total / len(nested_list)
    print("ID of lowest mark:", lowest)
    print("ID of highest mark:", highest)
    print("Average:", average)

    
fh = "students.txt"
students = []
student_info(students)

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")


def substitute(fh_in, fh_out, ciphertext):
    print()  # Leave a space between ciphertext and everything else
    message = open(fh_in).read()
    message = message.upper()
    message_list = [char for char in message]
    
    alphabet = "abcDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = [char for char in alphabet.upper()]
#     print("alphabet\t", alphabet)
    ciphertext = [char for char in ciphertext.upper()]
#     print("ciphertext\t", ciphertext)
    
    new_message_list = []
#     print()
#     print("message\t\t", message_list)
    
    for i in range(0, len(message_list), 1):
        # print("{} alphabet[i]".format(alphabet[i]))
        # print("{} alphabet.index(alphabet[i])".format(alphabet.index(alphabet[i])))
        if message_list[i] in alphabet:
            new_message_list.append(ciphertext[alphabet.index(message_list[i])])
        else:
            new_message_list.append(message_list[i])
#     print("new message list", new_message_list)
    new_message = ''.join(new_message_list)
#     print()
#     print("message\t\t", message)
#     print("new message\t", new_message)

    with open(fh_out, "a") as outfile:
        outfile.write(new_message)


fh_in = "pelee.txt"
fh_out = "pelee_substitute.txt"
print("Input file:", fh_in)
print("Output file:", fh_out)
ciphertext = input("Enter ciphertext:")
substitute(fh_in, fh_out, ciphertext)

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def shift(fh_in, fh_out, n):
    print()  # Leave a space
    message = open(fh_in).read()  # Import message from pelee.txt as a list
    message = message.upper()
    message_list = [char for char in message]
    
    alphabet = "abcDEFGHIJKLMNOPQRSTUVWXYZ"  # Create alphabet as list
    alphabet = [char for char in alphabet.upper()]
#     print("alphabet\t", alphabet)
    
    shifted_alphabet = []  # Create shifted alphabet
    for i in range(0, len(alphabet) - n, 1):
        shifted_alphabet.append(alphabet[i + n])
    for i in range(0, abs(len(alphabet) - len(shifted_alphabet)), 1):
        shifted_alphabet.append(alphabet[i])
#     print("shifted alpha\t", shifted_alphabet)

    new_message_list = []
    for i in range(0, len(message_list), 1):
        if message_list[i] in alphabet:
            new_message_list.append(shifted_alphabet[alphabet.index(message_list[i])])
        else:
            new_message_list.append(message_list[i])
    new_message = ''.join(new_message_list)  # Re-assemble new message list into one string
#     print("message\t\t", message)
#     print("new message\t", new_message)
    
    with open(fh_out, "a") as outfile:
        outfile.write(new_message)


fh_in = "pelee.txt"
fh_out = "pelee_shift.txt"
print("Input file:", fh_in)
print("Output file:", fh_out)
n = int(input("Enter shift: "))
shift(fh_in, fh_out, n)
