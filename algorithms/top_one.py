"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a 
representative value in an array.

For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]

"""

from collections import Counter


def top_one(array):
    dic_num = {}
    max_val = 0
    result = []
    for i in array:
        dic_num.update({i: array.count(i)})
    max_val=max(dic_num.values())
    for i in array:
        if array.count(i) == max_val and result.count(i) == 0 :
            result.append(i)
    return result,max_val


print(top_one([1, 2, 3, 4, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 2]))
