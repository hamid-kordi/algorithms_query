"""
move min :

[4,5,6,8,2,7,1,-1,4,-6] => [4,5,6,8,2,7,1,-1,4]

"""


def move_min(lst):
    temp = []
    minimum = 0
    for n in lst:
        if minimum > n:
            minimum = n

    for i in lst:
        if i != minimum:
            temp.append(i)
    return temp


### method


def move_min_method(lst):

    lst.remove(min(lst))
    return lst


print(move_min([4, 5, 6, 8, 2, 7, 1, -1, 4, -6]))
