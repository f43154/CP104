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
'''
# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
n = int(input("Enter n: "))
total = 0

for i in range(2, n + 1, 2):    
    total += i
    
print("The sum of all even numbers from 1 to {} is: {}".format(n, total))
