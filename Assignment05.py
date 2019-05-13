'''
Created on 2019 M05 9
__updated__ = '2019-05-13'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
Completed in ~ 2 hours 15 mins.
''' 
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

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
width = int(input("Width of diamond: "))
character = input("Printing character: ")
spaces = 0

if width % 2 == 0:
    for i in range(2, width + 1, 2):
        spaces = int((width - i) / 2)
        print(spaces * " " + i * character)

    for i in range(width - 2, 0, -2):
        spaces = int((width - i) / 2)
        print(spaces * " " + i * character)

else:
    for i in range (1, width + 1, 2):
        spaces = int((width - i) / 2)
        print(spaces * " " + i * character)
    
    for i in range(width - 2, 0, -2):
        spaces = int((width - i) / 2)
        print(spaces * " " + i * character)

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
integer = int(input("Number (>=1): "))
total = 0
inverse = 0
for i in range(1, integer + 1, 1):
    inverse = 1 / (i ** 2)
    total += inverse

print("\nSum of inverse squares for {} = {}".format(integer, total)) 

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
MONTHS_PER_YEAR = 12
years = int(input("Number of years of rainfall: "))
rainfall = 0
month = 0
total = 0
print("\nEnter rainfall in cm.\n")

for i in range(1, years + 1, 1):
    print("Year {}".format(i))
    for i in range(1, MONTHS_PER_YEAR + 1, 1):
        print("  Month", format(i), end="")
        rainfall = float(input(":"))
        total += rainfall
        month += 1

print("\nNumber of months: {}".format(month))
print("Total rainfall: {} cm".format(total))
average = total / month
print("Average rainfall per month: {} cm".format(average))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
num = int(input("Number of values: "))

value = int(input("\nFirst value: "))    
    
numNeg = 0
numZero = 0
numPos = 0
numEven = 0
numOdd = 0
total = value
minimum = value
maximum = value

if (value < 0):
    numNeg += 1        
if (value == 0):
    numZero += 1
if (value > 0):
    numPos += 1
if (value % 2 == 0):
    numEven += 1
if (value % 2 == 1):
    numOdd += 1
if (value > maximum):
    maximum = value
if (value < minimum):
    minimum = value
    
for i in range(1, num, 1):
    value = int(input("Next value: "))
    total += value
    if (value < 0):
        numNeg += 1        
    if (value == 0):
        numZero += 1
    if (value > 0):
        numPos += 1
    if (value % 2 == 0):
        numEven += 1
    if (value % 2 == 1):
        numOdd += 1
    if (value > maximum):
        maximum = value
    if (value < minimum):
        minimum = value
    
average = total / num
print("\nNegative values: \t{}".format(numNeg))
print("Zero values: \t\t{}".format(numZero))
print("Positive values: \t{}".format(numPos))
print("Even values: \t\t{}".format(numEven))
print("Odd values: \t\t{}".format(numOdd))
print("Total: \t\t\t{}".format(total))
print("Minimum: \t\t{}".format(minimum))
print("Maximum: \t\t{}".format(maximum))
print("Average: \t\t{}".format(average))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
starting = int(input("Starting value for table: "))
ending = int(input("Ending value for table: "))
row = 1
print("")
# VERTICAL COLUMN
for i in range(starting, ending + 1, 1):
    if row == 1:
        print("   ", end="")
        for i in range(starting, ending + 1, 1):
            print("{:>4}".format(i), end="")
        
        difference = (ending - starting) + 1
        print("\n   " + difference * 4 * "-")
        row += 1
        i = starting    
    
    print("{:<2}|".format(i), end="")
    
    # HORIZONTAL COLUMN
    for j in range(starting, ending + 1, 1):
        multiply = i * j
        print("{:>4}".format(multiply), end="")
    
    print("")
