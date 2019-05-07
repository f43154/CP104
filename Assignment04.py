'''
Created on 2019 M04 18
@author: Fani
Took about 2 hours to complete
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
HOT_DAYS = 28
PLEASANT_DAYS = 18
COLD_DAYS = 17

daily_temp = int(input("Temperature C (-500 to stop): "))
count = 0
num_hot = 0
num_pleasant = 0
num_cold = 0
total = 0

while daily_temp != -500:
    count += 1
    total += daily_temp
    
    if daily_temp >= 28:
        num_hot += 1
    elif daily_temp >= 18:
        num_pleasant += 1
    else:
        num_cold += 1

    daily_temp = int(input("Temperature C (-500 to stop): "))

print("\nCold days: \t{}".format(num_cold))
print("Pleasant days: \t{}".format(num_pleasant))
print("Hot days: \t{}".format(num_hot))
average = total / count
print("Average: {:.0f} C".format(average))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
current_pop = int(input("Current population: "))
growth_rate = int(input("Growth Rate (%): "))
target_pop = int(input("Target Population: "))
years = 0

while current_pop < target_pop:
    current_pop = current_pop * (1 + (growth_rate / 100))
    years += 1

print("\nIt will take {} year(s) to reach their target population.".format(years))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")
mothers_limit = int(input("Mom's limit on the number of candies: "))
candies = int(input("Candies from the first household: "))

while candies < mothers_limit:
    candies += int(input("Candies from the next household: "))

print("\nYou gathered {} candies in total.".format(candies))
leftover = candies - mothers_limit

if leftover > 0:
    print("You have {} candies over Mom's limit.".format(leftover))
else:
    print("You did not go over Mom's limit")

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
MIN_SPEND = .90

budget = float(input("Party budget: "))
min_budget = MIN_SPEND * budget
total = 0
another = "Y"
remaining = budget - total
print("")

while total < min_budget and another == "Y":
    cost = float(input("Cost of item: $"))
    total += cost
    
    if total > budget:
        total -= cost
        remaining = budget - total
        print("Item costs too much: ${:.2f} remaining in budget".format(remaining))
        another = "Y"
    
    another = input("Buy another item (Y/N): ")
    
    if another == "N" and total < min_budget:
        print("Have not yet spend the minimum amount: ${:.2f}".format(min_budget))
        another = "Y"  

remaining = budget - total
print("\nTotal spend on items: ${:.2f}".format(total))
print("Amount remaining: ${:.2f}".format(remaining))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
SENIOR_AGE = 65
SENIOR_PRICE = 4.0

ADULT_AGE = 18
ADULT_PRICE = 5.0

INFANT_AGE = 3
INFANT_PRICE = 0

STUDENT_AGE_LO = 10
STUDENT_AGE_HI = 15
STUDENT_PRICE = 1.0

KID_PRICE = 2.0

another = input("Purchase a ticket (Y/N)? ")
age = 0
total = 0
while another == "Y":
    age = int(input("How old are you? "))
    if age >= SENIOR_AGE:
        total += SENIOR_PRICE
        print("The ticket costs ${:.2f}".format(SENIOR_PRICE))
    elif age >= ADULT_AGE:
        total += ADULT_PRICE
        print("The ticket costs ${:.2f}".format(ADULT_PRICE))
    elif STUDENT_AGE_HI >= age >= STUDENT_AGE_LO:
        student = input("Are you a student at this school? (Y/N)? ")
        if student == "Y":
            total += STUDENT_PRICE
            print("The ticket costs ${:.2f}".format(STUDENT_PRICE))
        else:
            total += KID_PRICE
            print("The ticket costs ${:.2f}".format(KID_PRICE))
    elif age >= INFANT_AGE:
        total += KID_PRICE
        print("The ticket costs ${:.2f}".format(KID_PRICE))
    else:
        total += INFANT_PRICE
        print("The ticket costs ${:.2f}".format(INFANT_PRICE))

    another = input("Purchase another ticket (Y/N)? ")
    
print("Total tickets price: ${:.2f}".format(total))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")

# Imports
from random import randint

numQuestions = 0
numCorrect = 0
another = "Y"

while another == "Y":
    randOne = randint(0, 999)
    randTwo = randint(0, 999)
    print("\n{:>6}".format(randOne))
    print("+ {:>4}".format(randTwo))
    userEquals = int(input("= "))
    actualEquals = randOne + randTwo
    
    if userEquals == actualEquals:
        print("Congratulations!\n")
        numCorrect += 1
        numQuestions += 1
    else:
        print("Sorry, the correct answer is {}\n".format(actualEquals))
        numQuestions += 1
    
    another = input("Continue (Y/N): ")
    
print("\nYour final score is {}/{}".format(numCorrect, numQuestions))
