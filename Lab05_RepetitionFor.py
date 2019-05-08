'''
Created on 2019 M05 7
@author: Fani

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1, 2):    
    total += i
    
print("The sum of all odd numbers from 1 to {} is: {}".format(n, total))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
n = int(input("Enter n: "))
total = 0

for i in range(2, n + 1, 2):    
    total += i
    
print("The sum of all even numbers from 1 to {} is: {}".format(n, total))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")

n = int(input("Enter n: "))
total = 0
divided = 0
for i in range(1, n + 1, 1):
    divided = 1 / i
    total += divided
    
print("The sum of the series 1 to 1/{} is: {}".format(n, total))

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")
start = int(input("Enter start: "))
end = int(input("Enter end: "))
increment = int(input("Enter increment: "))
total = 0

for i in range(start, end + 1, increment):
    total += i

print("Total of {} to {} increment {}: {}".format(start, end, increment, total))

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")
num = int(input("Enter the number of values: "))
first = float(input("First value: "))
nextValue = 0
minimum = first
maximum = first
total = first
average = 0

for i in range(1, num, 1):
    nextValue = float(input("Next value: "))
    total += nextValue
    
    if maximum > nextValue:
        maximum = maximum
        minimum = nextValue
    else:
        maximum = nextValue
        minimum = minimum

average = total / num        
print("\nMinimum: {:.2f}".format(minimum))
print("Maximum: {:.2f}".format(maximum))
print("Total: {:.2f}".format(total))
print("Average: {:.2f}".format(average))

# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")
perMinute = float(input("Enter calories burned per minute: "))
beg = int(input("Enter beginning number of minutes: "))
ending = int(input("Enter ending number of minutes: "))
increment = int(input("Enter the increment in minutes: "))
print("")
total = 0

for i in range(beg, ending + 1, increment):
    total = (perMinute * i)
    print("Calories burned after {} minutes: {:.1f}".format(i, total))

# # # # # TASK 7 # # # # #
print("\n# # # # # TASK 7 # # # # #")
num = int(input("Enter number of bottles: "))
print("")

for i in range(num, 1, -1):
    print("{} bottles of beer on the wall, {} bottles of beer.\nTake one down, pass it around, {} bottles of beer on the wall.\n".format(i, i, i - 1))    

print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down, pass it around, no more bottles of beer on the wall!\n")
 
# # # # # TASK 8 # # # # #
print("\n# # # # # TASK 8 # # # # #")
RETIREMENT_AGE = 65
age = int(input("Enter the worker's age: "))
salary = float(input("Enter the worker's salary: "))
yearlyRaise = float(input("Enter the yearly raise (%): "))
print("\nAge         Salary\n------------------")
for i in range(age, RETIREMENT_AGE + 1, 1):
    print("{:>2}{:>16,.2f}".format(i, salary))
    salary += (yearlyRaise / 100) * salary

# # # # # TASK 9 # # # # #
print("\n# # # # # TASK 9 # # # # #")
purchaseValue = float(input("Enter the GIC purchase value: "))
years = int(input("Enter the number of years invested: "))
interest = float(input("Enter the GIC interest rate (%): "))
print("\nYear       Value $\n------------------")
for i in range(0, years + 1, 1):
    print("{:>2}{:>16,.2f}".format(i, purchaseValue))
    purchaseValue += (interest / 100) * purchaseValue

# # # # # TASK 10 # # # # #
print("\n# # # # # TASK 10 # # # # #")
width = int(input("Enter width of triangle: "))

for i in range(1, width + 1, 1):
    print((width - i) * ' ' + i * '#')
for i in range(width - 1, 0, -1):
    print((width - i) * ' ' + i * '#')

# # # # # TASK 11 # # # # #
print("\n# # # # # TASK 11 # # # # #")
width = int(input("Enter a number: "))
for i in range(1, width + 1, 1):
    print((width - i) * ' ' + i * '#' + (i - 1) * '#')
'''
# # # # # TASK 12 # # # # #
print("\n# # # # # TASK 12 # # # # #")
width = int(input("Enter a number: "))
last = 1

for i in range(1, width + 1, 1):
    
    if i < 4:
        last = i
    else:
        last = 0
        
    print("#" + (i - 2) * " " + (last - 1) * "#")

print("\n" + width * "#")
