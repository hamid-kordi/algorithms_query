"""
move zeros to end : 

[false,1,3,1,6,0,4,2,0,5] => [false,1,3,1,6,4,2,5,0,0]


"""

def move_zero(lst):
    temp = []
    count = 0
    for n in lst:
        if n != 0 or type(n)==bool :
            temp.append(n)
        elif n == 0 or type(n) != bool:
            count+=1
    for i in range(count):
        temp.append(0)
    return temp


print(move_zero([False,1,3,1,6,0,4,2,0,5]))
        

