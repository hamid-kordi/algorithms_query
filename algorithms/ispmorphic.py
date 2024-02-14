"""
the algorithms:

foo , doe => false
foo , dee => true

"""



def isomorphic(str1,str2):
    lst1=list(str1)
    lst2=list(str2)
    if len(lst1) == len(lst2):
        result = False
    return result