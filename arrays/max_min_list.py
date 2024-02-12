"""
in this we want
do this : 
 
array = [1, 2, 3, 4, 5, 6, 7, 8]
min = 3 => array_ch = [3, 4, 5, 6, 7, 8]
max = 3 => array_ch = [1, 2, 3]

"""


def check_input(array, min=None, max=None):

    check_min = lambda variable: True if min is None else (variable >= min)
    check_max = lambda variable: True if max is None else (variable <= max)

    return [x for x in array if check_max(x) and check_min(x)]


print(check_input([1, 2, 3, 4, 5, 6, 7, 8], 4, 7))
