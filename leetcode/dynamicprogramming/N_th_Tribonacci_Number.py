"""

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

"""


# itt is not a good code in time spent
class Solution_semi:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        else:
            result = (
                Solution.tribonacci(self, n - 1)
                + Solution.tribonacci(self, n - 2)
                + Solution.tribonacci(self, n - 3)
            )
            return result


# it is faster


class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0, 1, 1, 2, 4]
        if n > 4:
            for i in range(5, n + 1):
                temp = result[i - 1] + result[i - 2] + result[i - 3]
                result.append(temp)
        return result


"""
The following code is not for me,
    but it is a very good example
"""


class Solution_exm:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1

        T = [0, 1, 1]

        for index in range(3, n + 1):
            T[0], T[1], T[2] = T[1], T[2], T[0] + T[1] + T[2]

        return T[2]


obj = Solution()

print(obj.tribonacci(32))
