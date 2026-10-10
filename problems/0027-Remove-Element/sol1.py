# ==========================================================
# 27. Remove Element
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 55%)
# Link       : https://leetcode.com/problems/remove-element/
# ==========================================================

class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)
       
        