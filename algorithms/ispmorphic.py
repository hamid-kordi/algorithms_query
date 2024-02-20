"""
the algorithms:

foo , doe => False
foo , dee => True

"""


def isomorphic(str1: str, str2: str):
    result = 0
    lst1 = list(str1)
    lst2 = list(str2)
    len_les1 = len(lst1)
    len_les2 = len(lst2)
    if len_les1 != len_les2:
        result = 0
    else:
        i = 0  # pylint: disable=unused-variable
        result = 1

    return bool(result)


print(isomorphic("aef", "qwe"))
