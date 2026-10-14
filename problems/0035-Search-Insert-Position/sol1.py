# ==========================================================
# 35. Search Insert Position
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 1 ms (Beats 7%)
# Memory     : 12.9 MB (Beats 32%)
# Link       : https://leetcode.com/problems/search-insert-position/
# ==========================================================

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range (0,len(nums)):
            if nums[i] == target:
                return i
            else:
                nums.append(target)

        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i



        
        
        