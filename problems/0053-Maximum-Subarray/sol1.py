# ==========================================================
# 53. Maximum Subarray
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 98 ms (Beats 38%)
# Memory     : 21.1 MB (Beats 89%)
# Link       : https://leetcode.com/problems/maximum-subarray/
# ==========================================================

class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = nums[0]
        max_sum = cur_sum
        for num in nums[1:]:
            cur_sum = max(cur_sum+num, num)
            max_sum = max(cur_sum ,max_sum)

        return max_sum
        