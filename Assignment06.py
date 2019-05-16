'''
Created on 2019 M05 16
__updated__ = '2019-05-16'
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
Completed in 2 hours
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def get_brightness(wattage):
    if wattage == 15:
        return 125
    if wattage == 25:
        return 215
    if wattage == 40:
        return 500
    if wattage == 60:
        return 880
    if wattage == 75:
        return 1000
    if wattage == 100:
        return 1675
    else:
        return -1
    
   
wattage = int(input("Lightbulb wattage (w): "))
if wattage == -1:
    print("Invalid wattage")
else:
    print("Brightness: {} lumens".format(get_brightness(wattage)))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")


def payment(principal, interest, months):
    rate = (interest / 100) / months
    payment = (principal * rate) / (1 - ((1 + rate) ** (-months)))
    return payment


principal = float(input("Amount borrowed: $"))
interest = float(input("Interest rate: "))
months = int(input("Length of loan (months): "))
print("The monthly payment is ${:.2f}".format(payment(principal, interest, months)))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def get_total_change(n, d, q, l, t):
    tv = (n * 0.05) + (d * 0.10) + (q * 0.25) + (l * 1.00) + (t * 2.00)
    return tv


n = int(input("Enter number of nickels: "))
d = int(input("Enter number of dimes: "))
q = int(input("Enter number of quarters: "))
l = int(input("Enter number of loonies: "))
t = int(input("Enter number of toonies: "))
print("Total: ${:.2f}".format(get_total_change(n, d, q, l, t)))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")


def fraction_product(num1, den1, num2, den2):
    num = num1 * den2
    den = den1 * num2
    return num, den, num / den
    

num1 = float(input("Enter numerator of fraction 1: "))
den1 = float(input("Enter denominator of fraction 1: "))
num2 = float(input("Enter numerator of fraction 2: "))
den2 = float(input("Enter denominator of fraction 2: "))
print("Product = {0[0]:.0f}/{0[1]:.0f}\nDecimal = {0[2]}".format(fraction_product(num1, den1, num2, den2)))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def time_values(seconds):
    days = seconds / 86400
    hours = seconds / 3600
    minutes = seconds / 60
    return days, hours, minutes


seconds = int(input("Number of seconds: "))
print("\n{} seconds is the same as:".format(seconds))
print("\t{0[0]:.0f} days\n\t{0[1]:.0f} hours\n\t{0[2]:.0f} minutes".format(time_values(seconds)))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")
SECONDS_IN_DAYS = 86400
SECONDS_IN_HOURS = 3600
SECONDS_IN_MINUTES = 60


def time_split(initial_seconds):
    days = (initial_seconds - (initial_seconds % SECONDS_IN_DAYS)) / SECONDS_IN_DAYS
    seconds = initial_seconds - (SECONDS_IN_DAYS * days)
    hours = (seconds - (seconds % SECONDS_IN_HOURS)) / SECONDS_IN_HOURS
    seconds = seconds - (SECONDS_IN_HOURS * hours)
    minutes = (seconds - (seconds % SECONDS_IN_MINUTES)) / SECONDS_IN_MINUTES
    seconds = (seconds - (SECONDS_IN_MINUTES * minutes))
    return days, hours, minutes, seconds


initial_seconds = int(input("Number of seconds: "))
print("\nDays: {0[0]:.0f}, Hours: {0[1]:.0f}, Minutes: {0[2]:.0f}, Seconds: {0[3]:.0f}".format(time_split(initial_seconds)))

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")


def wall_area(width, height):
    area = width * height
    return area


def paint_required(area, standard_area):
    if area % standard_area != 0:
        total = (((area - (area % standard_area))) / standard_area) + 1
    else:
        total = area / standard_area
    return total


def hours_required(area, area_per_hour):
    if area % area_per_hour != 0:
        hours = (((area - (area % area_per_hour))) / area_per_hour) + 1
    else:
        hours = area / area_per_hour
    return hours


def paint_cost(total_paint, cost):
    pc = total_paint * cost
    return pc


print("Enter paint and labour standards:")
standard_area = float(input("Standard wall area (sq ft / gallon): "))
area_per_hour = float(input("Area painted per hour (sq ft / hour): "))
labour = float(input("Labour charges ($ / hour): "))

print("\nEnter customer information:")
cost = float(input("Cost of paint (1 gallon): $"))
height = float(input("Height of wall (ft): "))
width = float(input("Width of wall (ft): "))
print("\nPaint required: {:.0f} gallons".format(paint_required(wall_area(width, height), standard_area)))
print("Hours labour required: {:.0f} hours".format(hours_required(wall_area(width, height), area_per_hour)))
print("Paint cost:\t${:8.2f}".format(paint_cost(paint_required(wall_area(width, height), standard_area), cost)))
print("Labour cost:\t${:8.2f}".format(labour * hours_required(wall_area(width, height), area_per_hour)))
print("\t\t---------")
print("Total cost: \t${:8.2f}".format((paint_cost(paint_required(wall_area(width, height), standard_area), cost)) + (labour * hours_required(wall_area(width, height), area_per_hour))))
