# ==========================================================
# 283. Move Zeroes
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 11 ms (Beats 26%)
# Memory     : 13.7 MB (Beats 20%)
# Link       : https://leetcode.com/problems/move-zeroes/
# ==========================================================

class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for i in range (len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.pop(i)
                count = count + 1

        for i in range (count):
            nums.append(0)

        return nums
        