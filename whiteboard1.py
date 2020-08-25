'''
Write a function named same_values() that takes two lists of numbers of equal size as parameters.
The function should return a list of the indices where the values were equal in lst1 and lst2.
For example, the following code should return [0, 2, 3]
same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
'''
    #takes two lists of numbers of equal size
lst1 = [5, 1, -10, 3, 3]
lst2 = [5, 10, -10, 3, 5]

#function same values
def same_values(lst1, lst2):
    #list where values are equal will go
    sameVals = []
    for i in range(len(lst1)):
        print('lst1', i)
        
        for j in range(len(lst2)):
            print('lst2', j)
            # match = i == j
            # if match:
            if lst1[i] == lst2[j]:
                sameVals.append(i)
                
                #compare the two lists and add that value that is equal to a new list sameVals
                # now if lst1 or lst2 have a val that duplicates or is in sameVals then do not add to sameVals
                print('lst1 added', lst1[i])
                print('lst2 added', lst2[j])
                
                    
                print('same values', sameVals)     
   
    return sameVals
    
values = same_values(lst1,lst2)
print(values)
