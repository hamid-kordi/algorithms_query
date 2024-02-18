"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""



# v :1.10.0

def delete(lst, num_rep=1):
    """
    only for clean code :|
    """
    als = []
    for var in lst:
        if als.count(var) <num_rep:
            als.append(var)
    return als


print(delete([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6], 2))
