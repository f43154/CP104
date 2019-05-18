'''
Created on 2019 M05 17
__updated__ = '2019-05-17'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def is_hydroxide(chemical):
    return chemical.endswith("OH")


chemical = input("Enter a chemical formula: ")
if is_hydroxide(chemical) == True:
    print("{} is a hydroxide.".format(chemical))
else: 
    print("{} is not a hydroxide.".format(chemical))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")


def url_categorize(url):
    if url.endswith("com") == True:
        print("business")
    elif url.endswith("org") == True:
        print("non-profit")
    else:
        print("other")


url = input("Enter the website address: ")
url_categorize(url)

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def parse_code(product_code):
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


product_code = input("Enter a product code: ")
print("Category: \t{0[0]}\nID:\t\t{0[1]}\nQualifier:\t{0[2]}".format(parse_code(product_code)))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")


def validate_code(product_code):
    pc = product_code[0:3].isupper()
    pi = product_code[3:7].isdigit()
    pq = product_code[7:8].isupper() and product_code[8:].islower()
    return pc, pi, pq


product_code = input("Enter a product code: ")
if validate_code(product_code)[0] == True:
    print("Category {} is valid.".format(product_code[0:3]))
else:
    print("Category {} is not valid.".format(product_code[0:3]))

if validate_code(product_code)[1] == True:
    print("ID {} is valid.".format(product_code[3:7]))
else:
    print("ID {} is not valid.".format(product_code[3:7]))

if validate_code(product_code)[2] == True:
    print("Qualifier {} is valid.".format(product_code[7:]))
else:
    print("Qualifier {} is not valid.".format(product_code[7:]))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def password_strength(password):
    length = 0
    digits = 0
    uppercase = 0
    lowercase = 0
    for i in range(0, len(password), 1):
        if password[i:i + 1].isalnum() == True:
            length += 1
        if password[i:i + 1].isdigit() == True:
            digits += 1
        if password[i:i + 1].isupper() == True:
            uppercase += 1
        if password[i:i + 1].islower() == True:
            lowercase += 1
    if length < 8:
        print("not long enough")
    if digits == 0:
        print("no digits")
    if uppercase == 0:
        print("no upper case")
    if lowercase == 0:
        print("no lower case")


password = input("Enter a password: ")
password_strength(password)

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")


def is_palindrome(s):
    different = 0
    for i in range(0, len(s), 1):
        j = (len(s) - 1) - i
        if s[i] != s[j]:
            different += 1
    if different == 0:
        print("{} is a palindrome".format(s))
    else: 
        print("{} is not a palindrome".format(s))


s = input("Enter a string: ")
is_palindrome(s)

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def vowel_count(s):
    vowels = 0
    for i in range(0, len(s), 1):
        if s[i]in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            vowels += 1 
    print("There are {} vowels.".format(vowels))


s = input("Enter a string: ")
vowel_count(s)

# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")


def digits_count(s):
    digits = 0
    for i in range(0, len(s), 1):
        if s[i].isdigit():
            digits += 1 
    print("There are {} digits.".format(digits))


s = input("Enter a string: ")
digits_count(s)

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")


def count_special_char(s):
    special = 0
    for i in range(0, len(s), 1):
        if s[i]in ("#", "@", "$", "%", "&", "!"):
            special += 1 
    print("There are {} special characters.".format(special))


s = input("Enter a string: ")
count_special_char(s)
