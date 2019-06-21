'''
Created on 20 06 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''

# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")


def get_customer_record(file_handle, n): 
    file_handle = open("customers.txt", "r")   
    mylist = []
    mylist.append(file_handle.readlines()[n])
    
    if mylist[0][:1].isalnum() == True:
        print(mylist)
    else:
        print("[]")
    file_handle.close


n = int(input("Enter a record number: "))
file_handle = open("customers.txt", "r")  
get_customer_record(file_handle, n)
