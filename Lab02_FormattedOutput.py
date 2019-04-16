'''
Created on 2019 M04 2
@author: Fani
ID: 131581470
Email: hsie1470@mylaurier.ca

Completed in 2.5 hours
'''

# # # # # FORMAT TESTING # # # # #
# print("# # # # # FORMAT TESTING # # # # # \n") 
# phrase = "Hello World"
# print("|{:<15s}| :<15s Left Align\n".format(phrase))
# print("|{:^15s}| :^15s Centre Align\n".format(phrase))
# print("|{:>15s}| :>15s Right Align\n".format(phrase))
# print("|{:-^15s}| :-^15s\n".format(phrase))
# print("|{:->15s}| :->15s\n".format(phrase))
print("Referred to this a lot https://pyformat.info/")

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
line1 = "'I am Little Astronaut' by Jean Warren"
line2 = "I'm a little astronaut"
line3 = "Flying to the moon"
line4 = "My rocket is ready,"
line5 = "We blast off soon."
line6 = "I climb aboard"
line7 = "And close the hatch."
line8 = "5-4-3-2-1, off we blast!"

print("{:<23s}\n\n{:-^23s}\n    {:<23s}\n        {:<23s}\n        {:<23s}\n{:<23s}\n    {:<23s}\n        {:<23s}".format(line1, line2, line3, line4, line5, line6, line7, line8))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
print("'Twinkle Twinkle Little Star' by Jane Taylor\n")
print(0 * " " + "Twinkle, twinkle, little star,")
print(4 * " " + "How I wonder what you are!")
print(8 * " " + "Up above the world so high,")
print(8 * " " + "Like a diamond in the sky.")
print(0 * " " + "Twinkle, twinkle, little star,")
print(4 * " " + "How I wonder what you are!")

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
print('Selected quotes from Mark Twain:')
print('\"Do the right thing. It will gratify some people and astonish the rest.\"')
print('\"All generalizations are false, including this one.\"')
print('\"It is better to keep your mouth closed and let people think you are a fool\nthan to open it and remove all doubt.\"')

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
total = 500
percent = 10
math = total * (percent / 100)
print("A {} percent discount on {} is {}".format(percent, total, math))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
minimum = 38
maximum = 452
print("The difference between {} and {} is {}".format(maximum, minimum, maximum - minimum))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")
cost = 4.67
quantity = 5
print("Given a cost of {} and a quantity of {} the total is {}".format(cost, quantity, cost * quantity))

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")
breakfast = 6.75
lunch = 19.34
supper = 112.81
print("Meal\t\tCost\nBreakfast\t${:6.2f}\nLunch\t\t${:6.2f}\nSupper\t\t${:6.2f}\nTotal\t\t${:6.2f}".format(breakfast, lunch, supper, breakfast + lunch + supper))

# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")
dirt = 55.5
gravel = 30.6
sand = 112.8
print("Material\tCubic Metres\nDirt\t\t{:5.1f}\nGravel\t\t{:5.1f}\nSand\t\t{:5.1f}\nTotal\t\t{:5.1f}".format(dirt, gravel, sand, dirt + gravel + sand))

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")
sweatband = 4.95
pants = 23.27
jacket = 103.21
print("Clothes\t\tCost\nSweatband\t${:6.2f}\nPants\t\t${:6.2f}\nJacket\t\t${:6.2f}\nTotal\t\t${:6.2f}".format(sweatband, pants, jacket, sweatband + pants + jacket))

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")
month = 12
day = 8
year = 1990
print("{:1d}/{:02d}/{:02d}".format(year, month, day))

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")
location1 = "left"
location2 = "middle"
location3 = "right"
print("{:-<20s}\n{:-^20s}\n{:->20s}".format(location1, location2, location3))

# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")
first = 100
second = 34
third = 933
print("Values\nFirst:\t{:_>6d}\nSecond:\t{:_>6d}\nThird:\t{:_>6d}\nTotal:\t{:_>6d}".format(first, second, third, first + second + third))

# # # # # TASK 13 # # # # #
print("\n# # # # # TASK 13 # # # # #")
seconds = int(input("Enter the number of seconds: "))
# seconds = 3681
hours = (seconds // 3600)
minutes = ((seconds - (hours * 3600)) // 60)
remainingSeconds = (seconds - (minutes * 60) - (hours * 3600))
print("There are {} hours, {} minutes, and {} seconds in {} seconds".format(hours, minutes, remainingSeconds, seconds))

# # # # # TASK 14 # # # # #
print("\n# # # # # TASK 14 # # # # #")
minutes = int(input("Enter the number of minutes: "))
# minutes = 3369
days = minutes // (60 * 24)
hours = (minutes - (days * (60 * 24))) // 60
remainingMinutes = minutes - (days * (60 * 24)) - (hours * 60)
print("There are {} days, {} hours, and {} minutes in {} minutes".format(days, hours, remainingMinutes, minutes))

# # # # # TASK 15 # # # # #
print("\n# # # # # TASK 15 # # # # #")
integer = 654321
decimal = 654.32
phrase = "Hello World"
print("{}\t\t is integer as an integer".format(int(integer)))
print("{}\t is integer as an float".format(float(integer)))
print("{}\t\t is integer as an string".format(str(integer)))
print("{}\t\t is decimal as an integer".format(int(decimal)))
print("{}\t\t is decimal as an float".format(float(decimal)))
print("{}\t\t is decimal as an string".format(str(decimal)))
# print("{}\t\t is phrase as an integer".format(int(phrase))) ValueError: invalid literal for int() with base 10: 'Hello World'
# print("{}\t\t is phrase as an float".format(float(phrase))) ValueError: could not convert string to float: 'Hello World'
print("{}\t is phrase as an string".format(str(phrase)))
