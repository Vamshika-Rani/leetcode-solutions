# ==========================================================
# 1. Two Sum
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 2412 ms (Beats 8%)
# Memory     : 13.2 MB (Beats 39%)
# Link       : https://leetcode.com/problems/two-sum/
# ==========================================================

class Solution(object):
    def twoSum(self, nums, target):

      for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]
        