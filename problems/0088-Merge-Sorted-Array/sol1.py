# ==========================================================
# 88. Merge Sorted Array
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.4 MB (Beats 23%)
# Link       : https://leetcode.com/problems/merge-sorted-array/
# ==========================================================

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        merged = nums1[:m]
        for i in nums2:
            merged.append(i)
        merged.sort()
        nums1[:] = merged
        return nums1
 

        