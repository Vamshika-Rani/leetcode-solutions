# ==========================================================
# 217. Contains Duplicate
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 95 ms (Beats 5%)
# Memory     : 20.1 MB (Beats 96%)
# Link       : https://leetcode.com/problems/contains-duplicate/
# ==========================================================

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        