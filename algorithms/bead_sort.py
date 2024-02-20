"""
bead sort 
    [1,2,7,3,9,4,1,8,5] => [1,1,2,3,4,5,7,8,9 ]

"""


def bead_sort(setable):
    if any(not isinstance(x, int) or x < 0 for x in setable):
        raise TypeError("all of element in setable must be int")
    for _ in range(len(setable)):
        for i, (upp, loo) in enumerate(zip(setable, setable[1:])):
            if upp > loo:
                setable[i] -= upp - loo
                setable[i + 1] += upp - loo
        return setable


print(
    bead_sort([1, 345, 2, 8, 76, 123, 87, 4, 654, 2, 5, 80, 98, 643, 3, 67, 98, 75, 2])
)
