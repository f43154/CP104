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
    
    while(len(my_list) > 1):  # Stop when my_list is just the key
        
        if len(my_list) % 2 == 0:  # if length of list is even
            # print("\n// list is even lengthed //\n")
            
            right = my_list[int(len(my_list) / 2)]
            left = my_list[int((len(my_list) / 2) - 1)]
#             print("left:", left)
#             print("left index", int((len(my_list) / 2) - 1))
#             print("right:", right)
#             print("right index", int(len(my_list) / 2))
            
            if left > key:
                my_list = my_list[0:int((len(my_list) / 2))]        
                # new list after doing all the ifs
                # print("\nleft > key so new my_list", my_list)
                
                if right <= key:
                    print("list is not in order\nright {} > left {}".format(right, left))
                
            elif right > key:
                my_list = my_list[int((len(my_list) / 2) + 1):int(len(my_list))]  
                # new list after doing all the ifs
                print("\nright > key so new my_list", my_list)
                
            elif right == key and left < key:
                print("Index: {}".format(int(len(my_list) / 2)))
                # print("FOUND THE EARLIEST OCCURRENCE OF KEY AT {}".format(int(len(my_list) / 2)))
                my_list = [my_list[int(len(my_list) / 2)]]
                # print("\nright == key and left < key so new my_list", my_list)
            
            elif left == key:
                my_list = my_list[0:int((len(my_list) / 2) - 1)] 
                # new list after doing all the ifs
                # print("\nleft == key so new my_list", my_list)
            
            elif right < key:
                my_list = my_list[int(len(my_list) / 2):len(my_list)]
                # print("left < key so new my_list", my_list)
                
        elif len(my_list) % 2 == 1:
            # print("\nmy_list is odd lengthed: ", len(my_list))
            
            right = my_list[int(len(my_list) / 2)]
            left = my_list[int((len(my_list) / 2) - 1)]
            # print("left:", left)
            # print("left index:", int((len(my_list) / 2) - 1))
            # print("right:", right)
            # print("right index:", int(len(my_list) / 2))
            
            if left > key:
                my_list = my_list[0:int((len(my_list) / 2))] 
                # new list after doing all the ifs
                # print("\nleft > key so new my_list", my_list)
                
                if right <= key:
                    print("list is not in order\nright {} > left {}".format(right, left))
                
            elif left == key and right > key:
                my_list = my_list[0:int((len(my_list) / 2))] 
                # new list after doing all the ifs
                # print("\nleft == key so new my_list", my_list)
                
            elif right == key and left < key:
                print("Index: {}".format(int(len(my_list) / 2)))
                # print("FOUND THE EARLIEST OCCURRENCE OF KEY AT {}".format(int(len(my_list) / 2)))
                my_list = [my_list[int((len(my_list) / 2) + 1)]]
                # print("\nright == key and left < key so new my_list", my_list)
                
            elif right > key:
                my_list = my_list[int((len(my_list) / 2) + 1):int(len(my_list))]
                # new list after doing all the ifs
                # print("\nright > key so new my_list", my_list)
             
            elif right < key:
                my_list = my_list[int(len(my_list) / 2):len(my_list)]
                # print("left < key so new my_list", my_list) 

    
values = [2, 5, 5, 5, 5, 5, 5, 8]
# values = [2, 5, 5, 5, 5, 5, 5, 8]
print("Search: {} ".format(values), end="")
key = 5
print("for", key)
# key = int(input("for "))
binary_search(values, key)

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")
