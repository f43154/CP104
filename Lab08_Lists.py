'''
Created on 2019 M05 22
__updated__ = '2019-05-23'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
Completed in 3.5+ hours, stuck on Task 13 and 15
'''
''' 
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
DAYS_OF_THE_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def get_weekday_name(d):
    for i in range(d, d + 1, 1):
        print(DAYS_OF_THE_WEEK[i])
    

for d in range(7):
    get_weekday_name(d)

# # '# # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
MONTHS_OF_THE_YEAR = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def get_month_name(m):
    for i in range(m, m + 1, 1):
        print(MONTHS_OF_THE_YEAR[i])
        

for m in range(13):
    get_month_name(m)

# # '# # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
DIGITS_NAME = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_digit_name(n):
    for i in range(n, n + 1, 1):
        print(DIGITS_NAME[i])
        

for n in range(10):
    get_digit_name(n)

# # '# # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")

from random import randint


def generate_integer_list(n, low, high):
    values = []
    for n in range(0, n, 1):
        values.append(randint(low, high))
    return values


n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))
print("Values: ", generate_integer_list(n, low, high))

# # '# # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
from random import randint


def get_lotto_numbers(n, low, high):
    numbers = []
    for n in range(0, n, 1):
        numbers.append(randint(low, high))
    return numbers


n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))
print("Lotto Numbers: ", get_lotto_numbers(n, low, high))

# # '# # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")


def list_stats(values):
    smallest = values[0]
    largest = float()
    total = float()
    for i in range(0, len(values), 1):
        if values[i] < smallest:
            smallest = values[i]
        if values[i] > largest:
            largest = values[i]
        total += values[i]
    average = total / len(values)
    return smallest, largest, total, average


from random import randint


def generate_integer_list(n, low, high):
    values = []
    for n in range(0, n, 1):
        values.append(randint(low, high))
    return values


n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))
values = generate_integer_list(n, low, high)
print("Values: ", values)

print("Smallest value: {0[0]}\nLargest value: {0[1]}\nTotal: {0[2]}\nAverage: {0[3]}".format(list_stats(values)))

# # '# # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def generate_integer_list(n, low, high):
    from random import randint
    values = []
    for n in range(0, n, 1):
        values.append(randint(low, high))
    return values


n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))
values = generate_integer_list(n, low, high)
print("Values: ", values)


def list_categorize(values):
    negatives = 0
    positives = 0
    zeros = 0
    evens = 0
    odds = 0
    for i in range(0, len(values), 1):
        if values[i] < 0:
            negatives += 1
        if values[i] > 0:
            positives += 1
        if values[i] == 0:
            zeros += 1
        if values[i] % 2 == 0:
            evens += 1
        if values[i] % 2 == 1:
            odds += 1
    return negatives, positives, zeros, evens, odds


print("Negatives: {0[0]}\nPositives: {0[1]}\nZeroes: {0[2]}\nEvens: {0[3]}\nOdds: {0[4]}".format(list_categorize(values)))

# # '# # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")


def linear_search(a, v):
    for i in range(0, len(a), 1):
        index = -1
        if a[i] == v:
            index = i
            return index
            print(i)
            break
    return -1


from random import randint
a = []
for i in range(10):
    a.append(randint(-100, 100))
print("Values: ", a)

v = int(input("\nLinear search for: "))
print("Index of", v, ":", linear_search(a, v))


# # '# # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")

def linear_search(a, v):
    index = []
    for i in range(0, len(a) + 1, 1):
        if a[i] == v:
            index.append(i)
            return index


from random import randint
a = []
for i in range(10):
    a.append(randint(-100, 100))
print("Values: ", a)

v = int(input("\nLinear search for: "))
print("Index of", v, ":", linear_search(a, v))

# # '# # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")
from random import randint
a = []
for i in range(10):
    a.append(randint(-100, 100))
print("Values: ", a)


def min_search(a):
    smallest = a[0]
    indexes = []
    for i in range(len(a)):
        if a[i] < smallest:
            smallest = a[i]       
    for i in range(len(a)):
        if a[i] == smallest:
            indexes.append(i)
    return indexes


print("Indexes of minimums:", min_search(a))

# # '# # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")
from random import randint
source1 = []
source2 = []
for i in range(5):
    source1.append(randint(-5, 5))
    source2.append(randint(-5, 5))
print("Values: ", source1)
print("Values: ", source2)


def dot_product(source1, source2):
    target = []
    total = 0
    for i in range(len(source1)):
        target.append(source1[i] * source2[i])
    for i in range(len(target)):
        total += target[i]
    return total


print("\nDot product:", dot_product(source1, source2))

# # '# # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")
from random import randint
source1 = []
source2 = []
for i in range(5):
    source1.append(randint(-5, 5))
    source2.append(randint(-5, 5))
print("Values: ", source1)
print("Values: ", source2)


def dot_product(source1, source2):
    target = []
    for i in range(len(source1)):
        target.append(source1[i] + source2[i])
    return target


print("\nTotals:", dot_product(source1, source2))

# # '# # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")
from random import randint
source1 = []
source2 = []
for i in range(5):
    source1.append(randint(-5, 5))
    source2.append(randint(-5, 5))
print("Values: ", source1)
print("Values: ", source2)


def union(source1, source2):
    target = []
    united = []
    for i in range(len(source1)):
        target.append(source1[i])
    for i in range(len(source2)):
        target.append(source2[i])
        
    for x in target:        
        if x not in united:
            united.append(x)
    
    return united


print("Union:", union(source1, source2))

# # '# # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")
from random import randint
source1 = []
source2 = []
for i in range(randint(1, 10)):
    source1.append(randint(-5, 5))
for i in range(randint(1, 10)):
    source2.append(randint(-5, 5))
print("Values 1:", source1)
print("Values 2:", source2)


def intersection(source1, source2):
    intersection = []
    for i in range(len(source1)):
        for j in range(len(source2)):
            if source1[i] == source2[j]:
                intersection.append(source1[i])
    return intersection


print("\nIntersection:", intersection(source1, source2))
'''
# # '# # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")
from random import randint
source1 = []
source2 = []
for i in range(randint(1, 10)):
    source1.append(randint(-5, 5))
for i in range(randint(1, 10)):
    source2.append(randint(-5, 5))
print("Values 1:", source1)
print("Values 2:", source2)


def symmetric_difference(source1, source2):
    difference = []
    biglist = []
    for i in range(len(source1)):
        biglist.append(source1[i])
    for i in range(len(source2)):
        biglist.append(source2[i])
        
    for i in range(len(source1)):
        for j in range(len(biglist)):
            if source1[i] != biglist[j]:
                difference.append(source1[i])
    return difference

        
print(symmetric_difference(source1, source2))
