# ==========================================================
# 704. Binary Search
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 1 ms (Beats 3%)
# Memory     : 13.3 MB (Beats 73%)
# Link       : https://leetcode.com/problems/binary-search/
# ==========================================================

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1

