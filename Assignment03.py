'''
Created on 2019 M04 8
@author: Fani
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
numBalloons = int(input("Balloons collected: "))
if numBalloons >= 3:
    print("Bonus points earned: 50")
elif numBalloons >= 2:
    print("Bonus points earned: 25")
elif numBalloons >= 1:
    print("Bonus points earned: 10")
else:
    print("Bonus points earned: 0")

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
watts = int(input("Lightbulb wattage (w): "))
if watts == 100:
    print("Brightness: 1675 lumens")
elif watts == 75:
    print("Brightness: 1000 lumens")
elif watts == 60:
    print("Brightness: 880 lumens")
elif watts == 40:
    print("Brightness: 500 lumens")
elif watts == 25:
    print("Brightness: 215 lumens")
elif watts == 15:
    print("Brightness: 125 lumens")
else: 
    print("Invalid wattage")

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
player1 = input("Enter Player 1 choice (R, P, or S): ")
player2 = input("Enter Player 2 choice (R, P, or S): ")

if player1 == "R" and player2 == "R":
    print("A tie!")
if player1 == "P" and player2 == "P":
    print("A tie!")
if player1 == "S" and player2 == "S":
    print("A tie!")

if player1 == "R" and player2 == "P":
    print("Paper beats rock! Player 2 wins.")
if player1 == "R" and player2 == "S":
    print("Rock beats scissors! Player 1 wins.")
    
if player1 == "S" and player2 == "R":
    print("Rock beats scissors! Player 2 wins.")
if player1 == "S" and player2 == "P":
    print("Scissors beats paper! Player 1 wins.")
    
if player1 == "P" and player2 == "R":
    print("Paper beats rock! Player 1 wins.")
if player1 == "P" and player2 == "S":
    print("Scissors beats paper! Player 2 wins.")

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
primary1 = input("Enter first colour: ")
primary2 = input("Enter second colour: ")

if primary1 == "red" and primary2 == "red":
    print("No secondary colour")
if primary1 == "blue" and primary2 == "blue":
    print("No secondary colour")
if primary1 == "yellow" and primary2 == "yellow":
    print("No secondary colour")

if primary1 == "red" and primary2 == "blue":
    print("Secondary colour is purple")
if primary1 == "red" and primary2 == "yellow":
    print("Secondary colour is orange")
    
if primary1 == "yellow" and primary2 == "red":
    print("Secondary colour is orange")
if primary1 == "yellow" and primary2 == "blue":
    print("Secondary colour is green")

if primary1 == "blue" and primary2 == "red":
    print("Secondary colour is purple")
if primary1 == "blue" and primary2 == "yellow":
    print("Secondary colour is green")
else:
    print("No secondary colour")
    
# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
BASE_PRICE = 0.08
LENGTH_DISCOUNT = 0.10
length = int(input("Length of call (minutes): "))
hour = int(input("Hour of call (24 hour format): "))

if 18 <= hour < 24:
    starting_time_discount = 0.25
elif 0 <= hour <= 8:
    starting_time_discount = 0.50
else:
    starting_time_discount = 0
if length >= 30:
    length_discount = 0.10
else: 
    length_discount = 0

startPrice = (length * BASE_PRICE)
totalPrice = startPrice * (1 - starting_time_discount) * (1 - length_discount)  
print("Total price of call: ${:.2f}".format(totalPrice))
