'''
Created on 2019 M04 4
@author: Fani

Completed in 3 hours
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
DISCOUNT = 0.05
# membership = float(input("Gym membership cost: $"))
# numFriends = float(input("Number of friends signed up: "))
membership = 50
numFriends = 2
if numFriends >= 3:  # Limit maximum discount to 15% or 3 friends
    numFriends = 3
print("Your membership cost is ${:.2f}".format(membership - (numFriends * DISCOUNT * membership)))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
# target = float(input("Enter target: "))
# v1 = float(input("Enter v1: "))
# v2 = float(input("Enter v2: "))
target = 5.2
v1 = 3.4
v2 = 9.8
if abs(v1 - target) < abs(v2 - target):
    print("Closest value to {:0.1f} is {:0.1f}".format(target, v1))
elif abs(v1 - target) == abs(v2 - target):
    print("Closest value to {:0.1f} is {:0.1f}".format(target, v1))
else:
    print("Closest value to {:0.1f} is {:0.1f}".format(target, v2))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
year = int(input("Enter a year (>0): "))
if (year % 4) == 0:
    if (year % 400) == 0:
        print("{} is a leap year".format(year))
    elif (year % 100) != 0:
        print("{} is not a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
    
# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
age = int(input("Enter your age: "))
restHR = int(input("Enter your resting heart rate: "))
exerHR = int(input("Enter your heart rate during exercise: "))
maxHR = 220 - age
trainHR = int((((maxHR) - restHR) * 0.60) + restHR)
print("Your training heart rate is {}".format(trainHR))
if exerHR > trainHR:
    print("Keep up your exercise program")

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
totalPurchase = float(input("Total purchase: "))
isTeacher = str(input("Is the customer a teacher (Y/N)? "))
if isTeacher == "Y":
    print("Teacher's discount (10%):\t${:.2f}".format(totalPurchase * 0.10))
    print("Discounted total:\t\t${:.2f}".format(totalPurchase * 0.90))
    print("Sales tax\t\t\t${:.2f}".format((totalPurchase * 0.90) * 0.13))
    print("Total\t\t\t\t${:.2f}".format((totalPurchase * 0.90) * 1.13))
else:
    print("Sales tax\t\t\t${:.2f}".format(totalPurchase * 0.13))
    print("Total\t\t\t\t${:.2f}".format(totalPurchase * 1.13))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")
salary = int(round(float(input("Annual salary: "))))
yrsEmployed = int(input("Years employed: "))
if yrsEmployed < 2:
    print("You must have been employed for at least 2 years to qualify for a loan") 
if salary > 30000:
    print("You qualify for a loan!")
else:
    print("You must earn at least $30,000 per year to qualify for a loan")
   
# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")
test1 = int(input("Grade for test 1: "))
test2 = int(input("Grade for test 2: "))
test3 = int(input("Grade for test 3: "))
average = ((test1 + test2 + test3) / 3) 
print("The average: {:.0f}".format(average))
if average > 90:
    print("Congratulations, great average!")
    
# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")
rate = int(round(float(input("Hourly pay rate: "))))
hrs = int(input("Hours worked: "))
MAX_RATE = 40
if hrs > MAX_RATE:
    print("The week's pay is: ${:.2f}".format((rate * MAX_RATE) + ((hrs - MAX_RATE) * (rate * 1.5))))
else:
    print("The week's pay is: ${:.2f}".format(rate * hrs))

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")
print("For rectangle 1:")
length1 = float(input("Length of rectangle (cm): "))
width1 = float(input("Width of rectangle (cm): "))
area1 = length1 * width1

print("For rectangle 2:")
length2 = float(input("Length of rectangle (cm): "))
width2 = float(input("Width of rectangle (cm): "))
area2 = length2 * width2

print("\nArea of rectangle 1: {} cm^2".format(area1))
print("Area of rectangle 2: {} cm^2".format(area2))
if area1 > area2:
    print("Area of rectangle 1 is greater than area of rectangle 2.")
elif area1 == area2:
    print("The two areas are equal.")
else:
    print("Area of rectangle 2 is greater than area of rectangle 1.")

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")
GRAVITATIONAL_ACCELERATION = 9.8
kg = float(input("Enter mass (kg): "))
newtons = kg * GRAVITATIONAL_ACCELERATION
print("Weight: {:.2f} N".format(newtons))
if newtons > 1000:
    print("Object is too heavy")
if newtons < 10:
    print("Object is too light")
    
# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")
buryBarrels = int(input("Number of barrels to bury: "))
if (buryBarrels % 2) > 0 and buryBarrels > 2:
    barrelLength = int(float((buryBarrels / 2) + (1 / 2)))
    print("The size of the pit is 2 barrel(s) by {:.0f} barrel(s).".format(barrelLength)) 
    # print("The size of the pit is 2 barrel(s) by {} barrel(s).".format((buryBarrels / 2) + (buryBarrels % 2)))
if (buryBarrels % 2) == 0 and buryBarrels > 2:    
    print("The size of the pit is 2 barrel(s) by {:.0f} barrel(s).".format(buryBarrels / 2))    
if buryBarrels == 1:
    print("The size of the pit is 1 barrel(s) by 1 barrel(s).")
if buryBarrels == 2:
    print("The size of the pit is 1 barrel(s) by 2 barrel(s).")
   
# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")
number = int(input("Enter a number from 1 to 10: "))
if number == 10:
    roman = "X"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 9:
    roman = "IX"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 8:
    roman = "VIII"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 7:
    roman = "VII"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 6:
    roman = "VI"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 5:
    roman = "V"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 4:
    roman = "IV"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 3:
    roman = "III"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 2:
    roman = "II"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
elif number == 1:
    roman = "I"
    print("The roman numeral equivalent of {} is {}".format(number, roman))
else:
    print("None")

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")
windSpeed = int(input("Wind speed (km/h): "))
if windSpeed > 117:
    category = "Hurricane"
elif windSpeed > 89:
    category = "Whole Gale"
elif windSpeed > 62:
    category = "Gale Winds"
elif windSpeed > 39:
    category = "Strong Wind"
else:
    category = "Breeze"
print("Characterization: {}".format(category)) 

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")
richter = float(input("Richter Scale Number: "))
if richter > 7.5:
    category = "Catastrophe: most buildings destroyed"
    print(category) 
elif richter > 6.5:
    category = "Disaster: house and buildings may collapse"
    print(category) 
elif richter > 5.5:
    category = "Serious damage: Walls may crack or fall"
    print(category) 
elif richter > 5:
    category = "Some damage"
    print(category)  
else:
    category = "Little or no damage"
    print(category) 

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")
x_coordinate = float(input("Enter the x coordinate: "))
y_coordinate = float(input("Enter the y coordinate: "))
if x_coordinate > 0 and y_coordinate > 0:
    print("({:.2f}, {:.2f}) is in quadrant 1.".format(x_coordinate, y_coordinate))
if x_coordinate < 0 and y_coordinate > 0:
    print("({:.2f}, {:.2f}) is in quadrant 2.".format(x_coordinate, y_coordinate))
if x_coordinate < 0 and y_coordinate < 0:
    print("({:.2f}, {:.2f}) is in quadrant 3.".format(x_coordinate, y_coordinate))
if x_coordinate > 0 and y_coordinate < 0:
    print("({:.2f}, {:.2f}) is in quadrant 4.".format(x_coordinate, y_coordinate))
if x_coordinate == 0 and y_coordinate == 0:
    print("This is the origin")
if x_coordinate == 0 and y_coordinate != 0:
    print("({:.2f}, {:.2f}) is on the y axis.".format(x_coordinate, y_coordinate))
if y_coordinate == 0 and x_coordinate != 0 :
    print("({:.2f}, {:.2f}) is on the x axis.".format(x_coordinate, y_coordinate))
