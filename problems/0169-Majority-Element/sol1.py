# ==========================================================
# 169. Majority Element
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 5 ms (Beats 81%)
# Memory     : 13.7 MB (Beats 18%)
# Link       : https://leetcode.com/problems/majority-element/
# ==========================================================

class Solution(object):
    def majorityElement(self, nums):
       nums.sort()
       return nums[(len(nums)/2)]
        