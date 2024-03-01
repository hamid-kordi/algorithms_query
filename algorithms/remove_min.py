"""
move min :

[4,5,6,8,2,7,1,-1,4,-6] => [4,5,6,8,2,7,1,-1,4]

"""



def move_min(lst):
    temp = 0 
    minimum = 0 
    for n in lst:
        if minimum > n :
            minimum= n
    lst.remove(minimum)
    return lst


print(move_min([4,5,6,8,2,7,1,-1,4,-6]))