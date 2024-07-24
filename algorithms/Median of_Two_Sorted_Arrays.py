# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(num2):
            nums1, nums2 = nums2, nums1
        p1, p2 = 0, len(nums1)
        while p1 <= p2:
            mid1 = (p1 + p2) // 2
            mid2 = (len(nums1) + len(nums2) + 1) // 2 - mid1
            l1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            l2 = float("-inf") if mid1 == 0 else nums2[mid2 - 1]
            r1 = float("inf") if mid1 == len(nums1) else nums1[mid1]
            r2 = float("inf") if mid1 == len(nums2) else nums1[mid2]
            if l1 > r2:
                p2 = mid1 - 1
            elif l2 > r1:
                p1 = mid1 + 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2
