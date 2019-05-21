'''
Created on 2019 M05 21
__updated__ = '2019-05-21'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
Completed in 2 hours
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def my_isdigit(s):
    dgts = 0
    for i in range(0, len(s), 1):
        if s[i].isdigit() == False:
            dgts += 1
    if dgts > 0:
        return False
    else: 
        return True


s = input("Enter a string to test: ")
digits = my_isdigit(s)
if digits == True:
    print("The string is all digits")
else:
    print("The string contains non-digits")

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")


def my_isalpha(s):
    lttrs = 0
    for i in range(0, len(s), 1):
        if s[i].isalpha() == False:
            lttrs += 1
    if lttrs > 0:
        return False
    else: 
        return True
    

s = input("Enter a string to test: ")

if my_isalpha(s) == True:
    print("The string is all letters")
else:
    print("The string contains non-letters")

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def my_find(s, r):
    match = 0
    for i in range(0, len(s), 1):
        if r == s[i:i + len(r)]:
            match = i
    if match > 0:
        return match
    else:
        return -1


s = input("String to search: ")
r = input("String to search for: ")
print("'{}' is found at location {} in '{}'".format(r, my_find(s, r), s))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")


def common_ending(s1, s2):
    end = 0
    if len(s1) > len(s2):
        for i in range(1, len(s2) + 1, 1):
            if s1[len(s1) - i] == s2[len(s2) - i]:
                end += 1
            else:
                break
        print(s2[len(s2) - end:len(s2)])
    elif len(s2) > len(s1):
        for i in range(1, len(s1) + 1, 1):
            if s2[len(s2) - i] == s1[len(s1) - i]:
                end += 1
            else:
                break
        print(s1[len(s1) - end:len(s1)])
    else:
        for i in range(1, len(s1) + 1, 1):
            if s1[len(s1) - i] == s2[len(s2) - i]:
                end += 1
            else:
                break
        print(s1[len(s1) - end:len(s1)])

    
s1 = input("First string: ")
s2 = input("Second string: ")
print("Common ending: ", end="")
common_ending(s1, s2)

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def is_valid_isbn(isbn):
    dash = 0
    if len(isbn) == 17:
        if isbn[16].isdigit() and isbn[15] == "-":
            if isbn.startswith("978") or isbn.startswith("979"):
                for i in range(0, 17, 1):
                    if isbn[i] == "-":
                        dash += 1
                    else:
                        dash = 0
                    if dash > 1:
                        return False
                    if isbn[i].isdigit() or isbn[i] == "-":
                        if isbn[i] == "-":
                            dash += 1
                        if dash == 4:
                            return True
                        else:
                            return False
                    else:
                        return False
        else:
            return False
    else:
        return False
    
    
isbn = input("Enter an ISBN: ")
if is_valid_isbn(isbn) == True:
    print("This is a valid ISBN")
else:
    print(print("This is NOT a valid ISBN"))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")


def number_converter(number):
    for i in range(0, len(number), 1):
        if number[i] in ("A", "B", "C"):
            print("2", end="")
        elif number[i] in ("D", "E", "F"):
            print("3", end="")
        elif number[i] in ("G", "H", "I"):
            print("4", end="")
        elif number[i] in ("J", "K", "L"):
            print("5", end="")
        elif number[i] in ("M", "N", "O"):
            print("6", end="")
        elif number[i] in ("P", "R", "S"):
            print("7", end="")
        elif number[i] in ("T", "U", "V"):
            print("8", end="")
        elif number[i] in ("W", "X", "Y"):
            print("9", end="")
        else:
            print(number[i], end="")


number = input("Enter phone number: ")
print("Digits: ", end="")
number_converter(number)

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def pluralize(s):
    if s.endswith("s"):
        print("{}es".format(s))
    if s.endswith("ay"):
        print("{}s".format(s))
    elif s.endswith("y"):
        print("{}ies".format(s[0:len(s) - 1]))


s = input("Enter a string: ")
print("Plural: ", end="")
pluralize(s)

