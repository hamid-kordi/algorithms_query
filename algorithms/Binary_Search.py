# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            mean = (left + right) // 2
            if target > nums[mean]:
                left = mean + 1
            elif target < nums[mean]:
                right = mean - 1
            else:
                return mean
        return -1


# best solution :


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            mean = (left + right) // 2

            if target == nums[mean]:
                return mean

            if target < nums[mean]:
                right = mean - 1
            else:
                left = mean + 1

        return -1


obj = Solution()
print(obj.search([-1, 0, 3, 5, 9, 12], 9))
