"""
 6) Write a program that removes any repeated items from a list so that each 
 item appears at most
    once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

"""
a_list = [1,1,6,9,3,4,4,5,]
without_duplicates = []
for element in a_list:
    if element not in without_duplicates:
        without_duplicates.append(element)
print(without_duplicates)



