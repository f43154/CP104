'''
Created on 2019 M05 13
__updated__ = '2019-05-14'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
'''
from math import pi

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def sum_even(num):
    total = 0
    for i in range(2, num + 1, 2):
        total += i
    return total


number = int(input("Enter a number: "))
sumEven = sum_even(number)
print("The sum of all even numbers from 2 to {} is: {}".format(number, sumEven))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")


def sum_odd(num):
    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total


number = int(input("Enter a number: "))
total = sum_odd(number)
print("The sum of all odd numbers from 1 to {} is: {}".format(number, total))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def sum_partial_harmonic(num):
    total = 0
    for i in range(1, abs(num + 1), 1):
        total += (1 / i)
    return total


number = int(input("Enter n: "))
total = sum_partial_harmonic(number)
print("The sum of the series 1 to 1/{} is: {}".format(number, total))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")


def draw_rectangle(height, width, char):
    for height in range(0, height, 1):
        print(width * char)


height = int(input("Enter height in characters: "))
width = int(input("Enter width in characters: "))
char = input("Enter the draw character: ")
print("")
draw_rectangle(height, width, char)

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def draw_triangle(height, char):
    for i in range(0, height, 1):
        print(((height - 1) - i) * " " + (i + 1) * char + i * char)
        

height = int(input("Enter height in characters: "))
char = input("Enter the draw character: ")
draw_triangle(height, char)

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")


def draw_arrow(width, char):
    for i in range(1, width, 1):
        print(i * char)
    for j in range(width, 0, -1):
        print(j * char)


width = int(input("Enter width in characters: "))
char = input("Enter the draw character: ")
draw_arrow(width, char)

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def diametre(radius):
    diametre = radius * 2
    return diametre


def circumference(radius):
    circumference = 2 * pi * radius
    return circumference


def area(radius):
    area = pi * (radius ** 2)
    return area


radius = float(input("Enter radius: "))
print("\nDiametre of circle: {:.2f}".format(diametre(radius)))
print("Circumference of circle: {:.2f}".format(circumference(radius)))
print("Area of circle: {:.2f}".format(area(radius)))

# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year (>0): "))
if is_leap(year) == True:
    print("{} is a leap year".format(year))
else: 
    print("{} is not a leap year".format(year))

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")


def is_divisible(n, i, j):
    if n % i == 0 and n % j == 0:
        return True
    else:
        return False
    
    
n = int(input("Enter number to check for divisibility: "))
i = int(input("Enter first value to divide by: "))
j = int(input("Enter second value to divide by: "))

if is_divisible(n, i, j) == True:
    print("\n{} is evenly divisible by {} and {}.".format(n, i, j))
else: 
    print("\n{} is not evenly divisible by {} and {}.".format(n, i, j))

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")
TAX_RATE = 3.625
OVERTIME_HOURS = 40


def get_pay(hourly_rate, hours_worked):
    if hours_worked <= 40:
        return (hourly_rate * hours_worked) * (1 - (TAX_RATE / 100))
    else: 
        return ((hourly_rate * OVERTIME_HOURS) + ((hours_worked - OVERTIME_HOURS) * 1.5 * hourly_rate)) * (1 - (TAX_RATE / 100))


employee = int(input("Employee ID: "))
hourly_rate = float(input("Hourly wage rate: "))
hours_worked = float(input("Hours worked: "))
print("Net payment for employee {}: ${:,.2f}".format(employee, get_pay(hourly_rate, hours_worked)))

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")


def closest(target, v1, v2):
    if abs(v1 - target) <= abs(v2 - target):
        return v1
    else:
        return v2
    
    
target = float(input("Enter target: "))
v1 = float(input("Enter v1: "))
v2 = float(input("Enter v2: "))
print("Closest value to {} is {}".format(target, closest(target, v1, v2)))

# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")


def statistics(n):
    minimum = 0
    maximum = 0
    total = 0
    for i in range(1, n + 1, 1):
        value = float(input("Enter value {}:".format(i)))
        total += value
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value        
    print("\nMinimum: {:.2f}".format(minimum))
    print("Maximum: {:.2f}".format(maximum))
    print("Total: {:.2f}".format(total))
    average = total / n        
    print("Average: {:.2f}".format(average))


n = int(input("Enter number of values: "))
statistics(n)

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")


def square_pyramid(base, height):
    slant_height = (((base / 2) ** 2) + (height ** 2)) ** (1 / 2)
    print("\nSlant height of square pyramid: {:.2f}".format(slant_height))

    area = (base ** 2) + (2 * base) * ((((base ** 2) / 4) + (height ** 2)) ** (1 / 2))
    print("Area of square pyramid: {:.2f}".format(area))

    volume = (base ** 2) * (height / 3)
    print("Volume of square pyramid: {:.2f}".format(volume))


base = float(input("Length of base: "))
height = float(input("Perpendicular height of pyramid: "))
square_pyramid(base, height)

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")


def right_triangle(adjacent, opposite):
    h = ((adjacent ** 2) + (opposite ** 2)) ** (1 / 2)
    print("\nHypotenuse of triangle: {:.2f}".format(h))
    c = adjacent + opposite + h
    print("Circumference of triangle: {:.2f}".format(c))
    a = (adjacent * opposite) / 2
    print("Area of triangle: {:.2f}".format(a))


adjacent = float(input("Length of adjacent side: "))
opposite = float(input("Length of opposite side: "))
right_triangle(adjacent, opposite)

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")


def pythag(s1, s2):
    r = ((s1 ** 2) + (s2 ** 2)) ** (1 / 2)
    print("\nRadius of resulting circle: {:.2f}".format(r))
    d = 2 * r
    print("Diametre of resulting circle: {:.2f}".format(d))
    c = 2 * pi * r
    print("Circumference of resulting circle: {:.2f}".format(c))    
    a = pi * (r ** 2)
    print("Area of resulting circle: {:.2f}".format(a))

    
s1 = float(input("Length of side 1: "))
s2 = float(input("Length of side 2: "))
pythag(s1, s2)
