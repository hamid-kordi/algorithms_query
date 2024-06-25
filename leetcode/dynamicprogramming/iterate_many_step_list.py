"""
In this example, we are going to loop through a 
    list several times and see which order of counting and
    addition can create the largest sum. Every time the numbers are selected,
    there is a regular interval that is determined.
    
* >>>count
- >>>not count
for j == 0 and i == 0 >> *-*-*-*

for j == 0 and i == 1 >> -*-*-*-

for j == 1 and i == 0 >> *--*--*

for j == 1 and i == 1 >> -*--*--
"""

from typing import List
import math


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len > 2:
            count = 0
            result = {}
            step = math.floor(nums_len / 2)
            for j in range(step):
                for i in range(j + 2):
                    for k in range(step + 1):
                        if (j + 2) * k + i <= (nums_len - 1):
                            count = count + nums[(j + 2) * k + i]
                    result[f"{j}-{i}"] = count
                    count = 0

            return result[max(result, key=result.get)]

        else:
            return max(nums)


obj = Solution()
print(obj.rob([2, 7, 9, 3, 1]))
