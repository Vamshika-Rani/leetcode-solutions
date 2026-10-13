# ==========================================================
# 136. Single Number
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 10 ms (Beats 28%)
# Memory     : 13.4 MB (Beats 99%)
# Link       : https://leetcode.com/problems/single-number/
# ==========================================================

class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
            
        return nums[-1]