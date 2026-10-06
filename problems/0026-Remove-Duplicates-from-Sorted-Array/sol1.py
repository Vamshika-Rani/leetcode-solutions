# ==========================================================
# 26. Remove Duplicates from Sorted Array
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 5 ms (Beats 27%)
# Memory     : 13.9 MB (Beats 44%)
# Link       : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ==========================================================

class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.pop(i)

        return len(nums)
        