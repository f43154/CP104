'''
Created on 09 09 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def binary_search(values, key):
    my_list = list(values)
    print("list(values) ", list(values))
    print()
    
    while(len(my_list) > 1):  # Stop when my_list is just the key
        if len(my_list) % 2 == 0:  # if length of list is even
            print("\n// list is even lengthed //\n")
            middle = int(len(my_list) / 2)
            if key <= my_list[middle]:
                print("key <= my_list[middle]")
                my_list = my_list[0:middle]
                print("new my_list: \t", my_list)
                
            elif key > my_list[middle]:
                print("key > my_list[middle]")
                my_list = my_list[middle:len(my_list)]
                print("new my_list: \t", my_list)
                
        elif len(my_list) % 2 == 1:
            print("my_list is odd lengthed: ", len(my_list))

    print("\nfinal my_list", my_list)

    
values = [1, 2, 3, 4, 5, 6, 7, 8]  
# values = [2, 5, 5, 5, 5, 5, 5, 8]
print("Search: {} ".format(values), end="")
key = 4
print("for", key)
# key = int(input("for "))
binary_search(values, key)
