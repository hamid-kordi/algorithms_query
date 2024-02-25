"""

zigzag
[1,3,5,7,9] , [2,4,6,8] => [1,2,3,4,5,6,7,8,9] 

"""


class ZigZag:
    def __init__(self, l1, l2):
        self.quee = [l1, l2]

def next(self):
    v = self.quee.pop(0)
    r = v.pop(0)
    if v :
        self.quee.append(v)
    return r

    def have_next(self):
        if slef.quee:
            return True
        return False