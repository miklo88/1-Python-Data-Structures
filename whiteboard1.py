'''
Write a function named same_values() that takes two lists of numbers of equal size as parameters.
The function should return a list of the indices where the values were equal in lst1 and lst2.
For example, the following code should return [0, 2, 3]
same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
'''
#     #takes two lists of numbers of equal size
# lst1 = [5, 1, -10, 3, 3]
# lst2 = [5, 10, -10, 3, 5]
# # print(len(lst1))
# # for i in range(len(lst1)):
# #     print(lst1[i])
# #function same values
# def same_values(lst1, lst2):
#     #nested for loop lst one is the outer loop and lst 2 is the inner loop
#     #list where values are equal will go
#     sameVals = []
#     for i in range(len(lst1)):
#         print('lst1', lst1[i])
#         for j in range(len(lst2)):
#             print('lst2', lst2[j])
#             # so i have to remove the values that are equal from the lists so i dont get another match
#             #one and done deal.
#             if lst1[i] == lst2[j]:
#                 sameVals.append(i)
#     #returns a list where values are equal in lst1 and lst2
#     # return saveVals
#     print(sameVals)
# print(same_values(lst1, lst2))