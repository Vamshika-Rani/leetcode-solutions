# ==========================================================
# 349. Intersection of Two Arrays
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 20 ms (Beats 12%)
# Memory     : 12.3 MB (Beats 100%)
# Link       : https://leetcode.com/problems/intersection-of-two-arrays/
# ==========================================================

class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result
