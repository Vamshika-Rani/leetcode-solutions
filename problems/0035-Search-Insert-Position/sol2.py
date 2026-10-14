# ==========================================================
# 35. Search Insert Position
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 1 ms (Beats 7%)
# Memory     : 12.8 MB (Beats 67%)
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



        
        
        