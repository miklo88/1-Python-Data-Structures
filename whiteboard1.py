'''
Write a function named same_values() that takes two lists of numbers of equal size as parameters.
The function should return a list of the indices where the values were equal in lst1 and lst2.
For example, the following code should return [0, 2, 3]
same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
'''
    #takes two lists of numbers of equal size
lst1 = [5, 1, -10, 3, 3]
lst2 = [5, 10, -10, 3, 5]
# print(len(lst1))
# for i in range(len(lst1)):
#     print(lst1[i])
#function same values
def same_values(lst1, lst2):
    #nested for loop lst one is the outer loop and lst 2 is the inner loop
    #list where values are equal will go
    sameVals = []
    for i in range(len(lst1)):
        print('lst1', i)
        
        for j in range(len(lst2)):
            print('lst2', j)
            # so i have to remove the values that are equal from the lists so i dont get another match
            #one and done deal.
            match = i == j
            if match:
                sameVals.append(i)
                lst1.pop()
                lst2.pop()
                
                print('same values', set(sameVals))     
   
    return sameVals
    

values = same_values(lst1,lst2)
print(values)
