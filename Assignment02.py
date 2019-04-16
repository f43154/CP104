'''
Created on 2019 M04 8
@author: Fani
ID: 131581470
Email: hsie1470@mylaurier.ca
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
PROFIT_MARGIN = 0.18
sales1 = float(input("Enter projected annual sales: $"))
profit1 = PROFIT_MARGIN * sales1
print("The projected profit on sales of ${:,.2f} is ${:,.2f}.\n".format(sales1, profit1))

sales2 = float(input("Enter projected annual sales: $"))
profit2 = PROFIT_MARGIN * sales2
print("The projected profit on sales of ${:,.2f} is ${:,.2f}.\n".format(sales2, profit2))

sales3 = float(input("Enter projected annual sales: $"))
profit3 = PROFIT_MARGIN * sales3
print("The projected profit on sales of ${:,.2f} is ${:,.2f}.\n".format(sales3, profit3))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
STUDENT_DISCOUNT = 1 - 0.2
cost = float(input("Cost of movie: $"))
studentCost = cost * STUDENT_DISCOUNT
print("The cost of the movie for a student is ${:.2f}.\n".format(studentCost))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
PRICE_LARGE = 75
PRICE_SMALL = 50
numLarge = int(input("Number of large dogs groomed: "))
numSmall = int(input("Number of small dogs groomed: "))
profit = PRICE_LARGE * numLarge + PRICE_SMALL * numSmall
print("Total earned for the day: ${:,.2f}.".format(profit))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
borrowed = int(input("Amount borrowed: $"))
interest = int(input("Interest rate: "))
length = float(input("length of loan (months): "))
monthly_interest = (interest / 100) / 12
one_plus_monthly_interest = 1 + monthly_interest
brackets_to_power_months = one_plus_monthly_interest ** (-length)
one_minus_brackets = 1 - brackets_to_power_months
monthlyPMT = (monthly_interest * borrowed) / (one_minus_brackets)
print("The monthly payment is ${:,.2f}.".format(monthlyPMT))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
PI = 3.14
radius = float(input("Diameter of container base (cm): ")) / 2
height = float(input("Height of container (cm): "))
cost = float(input("Cost of materials ($/cm^2): "))
num = float(input("Number of containers: "))
area_circle = PI * (radius ** 2)
circumference = 2 * PI * radius
area_cylinder = circumference * height
cost_One = (area_circle + area_cylinder) * cost
cost_All = cost_One * num
print("The cost of one container is :${:,.2f}".format(cost_One))
print("The total cost of all containers i ${:,.2f}".format(cost_All))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")
flyers = int(input("Number of flyers: "))
volunteers = int(input("Number of volunteers: "))
per_volunteer = int(flyers / volunteers)
leftover = int(flyers % volunteers)
print("Flyers per volunteer: {}".format(per_volunteer))
print("Flyers left over: {}".format(leftover))
