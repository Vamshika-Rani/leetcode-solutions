# ==========================================================
# 268. Missing Number
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 17 ms (Beats 27%)
# Memory     : 13.3 MB (Beats 69%)
# Link       : https://leetcode.com/problems/missing-number/
# ==========================================================

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range (0,len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
        