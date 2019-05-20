'''
Created on 2019 M05 17
__updated__ = '2019-05-20'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
Completed in ~2 hours
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

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")


def text_analyze(txt):
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    for i in range(0, len(txt), 1):
        if txt[i].isupper() == True:
            uppr += 1
        if txt[i].islower() == True:
            lowr += 1
        if txt[i].isdigit() == True:
            dgts += 1
        if txt[i].isspace() == True:
            whtspc += 1
    return uppr, lowr, dgts, whtspc
    

txt = input("Enter a string: ")
text_analyze(txt)
print("\nupper case letters: {0[0]}\nlower case letters: {0[1]}\ndigits: {0[2]}\nwhitespace: {0[3]}".format(text_analyze(txt)))

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")


def dsmvwl(s):
    for i in range(0, len(s), 1):
        if s[i]in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            print("", end="")
        else:
            print("{}".format(s[i]), end="")


s = input("Enter a string: ")
dsmvwl(s)

# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")


def comma_period_replace(s):
    for i in range(0, len(s), 1):
        if s[i] == ",":
            print(".", end="")
        else:
            print(s[i], end="")
            
            
s = input("Enter a string: ")
comma_period_replace(s)

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")


def total_digits(s):
    digits = 0
    for i in range(0, len(s), 1):
        if s[i].isdigit() == True:
            digits += float(s[i])
    return digits


s = input("Enter a string: ")
print("Digits total: {:.0f}".format(total_digits(s)))

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")


def str_distance(s1, s2):
    distance = 0
    if len(s1) == len(s2):
        for i in range(0, len(s1), 1):
            if s1[i] != s2[i]:
                distance += 1
    else: 
        distance = -1
    return distance


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Distance: {}".format(str_distance(s1, s2)))

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")


def calculate(expr):
    for i in range(0, len(expr), 1):
        if expr[i] == "+":
            result = float(expr[0]) + float(expr[4])
        if expr[i] == "-":
            result = float(expr[0]) - float(expr[4])
        if expr[i] == "*":
            result = float(expr[0]) * float(expr[4])
        if expr[i] == "/":
            result = float(expr[0]) / float(expr[4])
        if expr[i] == "%":
            result = float(expr[0]) % float(expr[4])
    return result       

    
expr = input("Enter an expression: ")
print("{} = {:.0f}".format(expr, calculate(expr)))
