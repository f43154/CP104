'''
Created on 10 06 2019
__updated__ = ''
Author: Fani
ID: 123456789
Email: email@mylaurier.ca
@author: Fani
'''
'''
# # # # # TASK 1 # # # # #
print("\n# # # # # TASK 1 # # # # #")

from random import choices


def bag_to_set(bag):
    new_set = []
    for i in range(0, len(bag), 1):
        if bag[i] not in new_set:
            new_set.append(bag[i])
    return new_set


bag = choices(range(10), k=5)
print("Bag: ", bag)
print("Set: ", bag_to_set(bag))

# # # # # TASK 2 # # # # #
print("\n# # # # # TASK 2 # # # # #")

from random import choices


def clean_list(values):
    new_values = []
    for i in range(0, len(values), 1):
        if values[i] not in new_values:
            new_values.append(values[i])    
    values = new_values
    return values


values = choices(range(5), k=10)
print("Values:\t", values)
print("Cleaned: ", clean_list(values))

# # # # # TASK 3 # # # # #
print("\n# # # # # TASK 3 # # # # #")


def two_element_subset(string):
    subset = []
    for i in range(0, len(string), 1):
        j = i + 1
        while j < len(string):
            subset.append(string[i] + string[j])
            j += 1
    print("Subsets: ", subset)

    
string = input("String: ")
two_element_subset(string)

# # # # # TASK 4 # # # # #
print("\n# # # # # TASK 4 # # # # #")

from random import randint


def set_trials(subjects):
    for i in range(0, len(subjects), 1):
        random = randint(0, 1)
        if random == 1:
            drugs.append(subjects[i])
        else:
            placebos.append(subjects[i])
    
    if len(subjects) % 2 == 0:
        while len(drugs) != len(placebos):        
            if len(drugs) > len(placebos):
                placebos.append(drugs[len(drugs) - 1])
                drugs.pop()
            elif len(drugs) < len(placebos):
                drugs.append(placebos[len(placebos) - 1])
                placebos.pop()
    
    if len(subjects) % 2 == 1:
        while (len(drugs) - 1) != len(placebos):
            if len(drugs) > len(placebos):
                placebos.append(drugs[len(drugs) - 1])
                drugs.pop()
            elif len(drugs) < len(placebos):
                drugs.append(placebos[len(placebos) - 1])
                placebos.pop()        


subjects = ["David", "Tasmin", "Tristan", "Lori", "Kate", "Li-Meng"]
drugs = []
placebos = []
print("Subjects:\t", subjects)
set_trials(subjects)
print("Drug trial: \t", drugs)
print("Placebo trial:\t", placebos)

# # # # # TASK 5 # # # # #
print("\n# # # # # TASK 5 # # # # #")


def license_test(correct_answers, student_answers):    
    correct = 0
    incorrect = 0
    indexes = []
    for i in range(0, len(correct_answers), 1):
        if correct_answers[i] == student_answers[i]:
            correct += 1
        else:
            incorrect += 1
            indexes.append(i)
    print("Correct Answers Count: ", correct)
    print("Incorrect Answers Count: ", incorrect)
    print("Indexes of incorrect answers: ", indexes)


from random import choices
correct_answers = choices(range(3), k=5)
student_answers = choices(range(3), k=5)
print("Correct Answers: ", correct_answers)
print("Student Answers: ", student_answers)
license_test(correct_answers, student_answers)

'''
# # # # # TASK 6 # # # # #
print("\n# # # # # TASK 6 # # # # #")

