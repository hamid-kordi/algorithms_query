# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        seen = dict()
        result = 0
        for p2 in range(len(s)):
            char = s[p2]
            if char in seen and seen[char] >= p1:
                print(seen[char])
                p1 = seen[char] + 1
            else:
                result = max(result, p2 - p1 + 1)

            seen[char] = p2

        return result


obj = Solution()
print(obj.lengthOfLongestSubstring("tmmzuxt"))
