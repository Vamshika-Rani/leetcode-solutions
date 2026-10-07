# ==========================================================
# 75. Sort Colors
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 3 ms (Beats 18%)
# Memory     : 12.5 MB (Beats 20%)
# Link       : https://leetcode.com/problems/sort-colors/
# ==========================================================

class Solution(object):
    def sortColors(self, nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]

        return nums