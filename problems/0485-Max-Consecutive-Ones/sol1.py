# ==========================================================
# 485. Max Consecutive Ones
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 45 ms (Beats 12%)
# Memory     : 16.1 MB (Beats 25%)
# Link       : https://leetcode.com/problems/max-consecutive-ones/
# ==========================================================

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                count = 0

            max_count = max(count, max_count)

        return max_count