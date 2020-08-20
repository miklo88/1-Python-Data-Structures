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
'''
Print out all of the strings in the following array that represent a number divisible by 3:
[
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]
The expected output for the above input is:
nine hundred ninety nine
twelve
eighteen
six
twelve
'''
# if num is divisible by three. return the num 
#if i wanted to i could store the return True values in a list
# just going to be looping through the list
# doing mathematical problems not with integers but with strings.
# looking up list data. looking up strings and accomadating math to them.
nums = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

# print(nums)
# for i in nums:
# # for i in range(10):
#     if i % 3 == 0:
#         print(i)
#     else:
#         pass
#     # print(i)
    
