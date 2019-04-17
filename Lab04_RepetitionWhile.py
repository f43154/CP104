'''
Created on 2019 M04 5
@author: Fani

Completed in ~ 4.5 hours
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
from random import randint
number = randint(0, 100)
guess = int(input("Guess: "))

while guess != number:
    if guess > number:
        print("Too high, try again.")
        guess = int(input("Guess: "))
    if guess < number:
        print("Too low, try again.")
        guess = int(input("Guess: "))
print("Congratulations - good guess!")

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")

another = "Y"
day = 1
total_breakfast = 0
total_lunch = 0
total_supper = 0
total_grand = 0

while another == "Y":
    print("For Day {}\n".format(day))
    day += 1
    breakfast = float(input("How much was breakfast? $"))
    total_breakfast += breakfast
    lunch = float(input("How much was lunch $"))
    total_lunch += lunch
    supper = float(input("How much was supper? $"))
    total_supper += supper
    totalday = breakfast + lunch + supper
    total_grand += totalday
    print("Your total for the day was ${:.2f}\n".format(totalday))
    another = input("Were you away another day (Y/N)? ")
    print("\n")
print("Total:\nBreakfast: \t${:>5.2f}\nLunch: \t\t${:>5.2f}\nSupper: \t${:>5.2f}\n\nGrand total: \t${:>5.2f}".format(
    total_breakfast, total_lunch, total_supper, total_grand))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
target_number = int(input("Enter target number: "))
base = 0
power_of_two = 0 
while power_of_two < target_number:
    base += 1 
    power_of_two = 2 ** base
print("The nearest power of 2 >= {} is {}.".format(target_number, power_of_two))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
budget = float(input("Monthly budget: $"))
expense = float(input("Enter an expense (0 to quit): $"))
while expense != 0:
    budget = budget - expense
    expense = float(input("Enter another expense (0 to quit): $"))
if budget > 0:
    print("Surplus: ${:7.2f}".format(budget))
if budget < 0:
    print("Deficit: ${:7.2f}".format(budget))
if budget == 0:
    print("Balanced: ${:7.2f}".format(budget))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
budget = float(input("Enter budget: $"))
expense = float(input("Expenses for day 1: $"))
day = 1
while day < 7:
    day += 1
    print("Expenses for day {}".format(day), end="")
    expense += float(input(": "))

budget = budget - expense
print("Expenses:\t${:11,.2f}".format(expense))
print("Balance:\t${:11,.2f}".format(budget))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")
value = float(input("First value: "))
total_value = value
cycle = 0
while value != 0:
    value = float(input("Next value: "))
    total_value += value
    cycle += 1
average = total_value / (cycle)
print("\nTotal: {:.2f}".format(total_value))
print("Average: {:.2f}".format(average))

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")
value = float(input("First value: "))
maximum = 0
minimum = 0
while value != 0:
    value = float(input("Next value: "))
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value

print("Minimum: {:.1f}".format(minimum))
print("\nMaximum: {:.1f}".format(maximum))

# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")
value = float(input("First value: "))
positive = 0
negative = 0
while value != 0:
    if value > 0:
        positive += 1
    if value < 0:
        negative += 1
    value = float(input("Next value: "))

print("\nNumber of positive values: {}".format(positive))
print("Number of negative values: {}".format(negative))

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")
start_celsius = int(input("Starting Celsius temperature: "))
end_celsius = int(input("Ending Celsius temperature: "))
fahrenheit = 0
print("\nCelsius Fahrenheit\n------------------")

if start_celsius > end_celsius:
    while start_celsius != end_celsius:
        print("{:>7}".format(start_celsius), end="")
        fahrenheit = int(9 / 5 * start_celsius + 32)
        print("{:>11}".format(fahrenheit)) 
        start_celsius -= 1
        
if start_celsius < end_celsius:
    while start_celsius < end_celsius:
        print("{:>7}".format(start_celsius), end="")
        fahrenheit = int(9 / 5 * start_celsius + 32)
        print("{:>11}".format(fahrenheit)) 
        start_celsius += 1

print("{:>7}".format(start_celsius), end="")
fahrenheit = int(9 / 5 * start_celsius + 32)
print("{:>11}".format(fahrenheit))         

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")
start_fahrenheit = int(input("Starting Fahrenheit temperature: "))
end_fahrenheit = int(input("Ending Fahrenheit temperature: "))
celsius = 0
print("\nFahrenheit Celsius\n------------------")

if start_fahrenheit > end_fahrenheit:
    while start_fahrenheit != end_fahrenheit:
        print("{:>10}".format(start_fahrenheit), end="")
        celsius = int(round((5 / 9) * (start_fahrenheit - 32)))
        print("{:>8}".format(celsius)) 
        start_fahrenheit -= 1
        
if start_fahrenheit < end_fahrenheit:
    while start_fahrenheit < end_fahrenheit:
        print("{:>10}".format(start_fahrenheit), end="")
        celsius = int(round((5 / 9) * (start_fahrenheit - 32)))
        print("{:>8}".format(celsius)) 
        start_fahrenheit += 1

print("{:>10}".format(start_fahrenheit), end="")
celsius = int(round((5 / 9) * (start_fahrenheit - 32)))
print("{:>8}".format(celsius))         

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")
TAX = 0.03625
OVERTIME = 1.5
NUM_OVERTIME = 40

total_payment = 0
average_count = 0
gross_wage = 0
net_payment = 0
employee_id = int(input("Employee ID: "))

while employee_id > 0:
    hourly_rate = int(input("Hourly wage rate: "))
    hours_worked = int(input("Hours worked: "))
    
    if hours_worked > 40:
        gross_wage = hourly_rate * OVERTIME * (hours_worked - NUM_OVERTIME) + hourly_rate * NUM_OVERTIME
    else:
        gross_wage = hourly_rate * hours_worked
        
    net_payment = gross_wage * (1 - TAX)
    total_payment += net_payment
    average_count += 1
    print("Net payment for employee {}: ${:,.2f}\n".format(employee_id, net_payment)) 
    employee_id = int(input("Employee ID: "))
    
print("---------------------------")
average_payment = total_payment / average_count
print("Total payment: \t\t${:>9,.2f}".format(total_payment))
print("Average payment: \t${:>9,.2f}".format(average_payment))

# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")
min_value = int(input("Enter the min value: "))
max_value = int(input("Enter the max value: "))
print("Enter an integer {} <= n <= {}".format(min_value, max_value), end="")
entered_value = int(input(": "))
while entered_value > max_value or entered_value < min_value:
    print("Bad value!")
    print("Enter again {} <= n <= {}".format(min_value, max_value), end="")
    entered_value = int(input(": "))
print("You entered: {}".format(entered_value))

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")
integer = abs(int(input("Enter an integer: ")))
factorialed = 1
print("{}! = ".format(integer), end="")
while integer > 0:
    factorialed *= integer
    print("{}".format(integer), end="")
    integer -= 1
    if integer > 0:
        print(" * ".format(integer), end="")    
    else: 
        print(" ", end="")
print("= {:,}".format(factorialed))

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")
integer = int(input("Enter an integer: "))
factorialised = integer
prime = 0

while factorialised > 0:
    if integer % factorialised == 0:
        prime += 1
    factorialised -= 1

if prime == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")
value = float(input("First value: "))
maximum = value
minimum = value
count = 0
total = 0

while value != 0:
    total += value
    value = float(input("Next value: "))
    count += 1
    
    if value > maximum:
        maximum = value
    elif value < minimum:
        minimum = value

average = total / count    
print("\nMinimum: {:.2f}".format(minimum))
print("Maximum: {:.2f}".format(maximum))
print("Total: {:.2f}".format(total))
print("Average: {:.2f}".format(average))
