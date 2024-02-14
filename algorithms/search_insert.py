"""
[1,2,3,4] , 3 => 2,
[1,2,6,7] , 4 => 2,
[1,2,3,4] , 7 => 4,
[1,2,4,5] , 0 => 0 

"""

def serch_insert(array, N):
    if N in array:
        result = array.index(N)
    else:
        array.append(N)
        array.sort()
        result = array.index(N)
    return result



"""
About this section:
    We proceed with three assumptions
    * In the first case, our number is smaller than the smallest number in the list    
    * Or our number is greater than the largest number in the list
    * Or it is between these two values and between two other values in our list

-- The list is sorted

"""


def search_insert_hand(array,N):
    array.sort()
    if N in array:
        result = array.index(N)
    else:
        for i in array:
            if N <= array[0] and array.index(i) == 0 :
                array.insert(0,N)
            elif N > array[len(array)-1] and array.index(i) == (len(array)-1) : 
                array.insert(len(array),N)
            elif N>i and N<= array[array.index(i) + 1]:
                array.insert(array.index(i)+1,N)
    result = array.index(N)
    return result



print(search_insert_hand([1, 5, 6, 7, 3, 4], 2))
