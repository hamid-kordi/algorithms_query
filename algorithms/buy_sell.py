"""
You buy at the first point and sell at the next point
You need to find out which of them sells the most profit :
[1th month, 2th month, 3th month, 4th month,]
[7, 1, 5, 3, 6, 4] => 5
[9, 7, 6, 4, 3, 1] => 0
"""


def buy_sell(lst):
    buy_in = 0
    max_profit = 0
    month_rate = 0
    lst2 = lst.copy()

    lst2.pop(len(lst2) - 1)

    for i in lst2:
        buy_in = i
        benefit = lst[lst.index(i) + 1] - buy_in
        if benefit > 0 and benefit > max_profit:
            max_profit = benefit
            month_rate = lst[lst.index(i) + 1]
    return month_rate


print(buy_sell([10,2,4,5,7,2,4,1]))
