"""

zigzag
[1,3,5,7,9] , [2,4,6,8,10] => [1,2,3,4,5,6,7,8,9,10] 

"""


class ZigZag:
    def __init__(self, l1, l2):
        self.quee = [l1, l2]

    def next(self):
        v = self.quee.pop(0)
        r = v.pop(0)
        if v:
            self.quee.append(v)
        return r

    def have_next(self):
        if self.quee:
            return True
        return False


z = ZigZag([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
while z.have_next():
    print(z.next())
