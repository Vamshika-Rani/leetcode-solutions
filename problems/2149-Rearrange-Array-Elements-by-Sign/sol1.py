# ==========================================================
# 2149. Rearrange Array Elements by Sign
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 131 ms (Beats 16%)
# Memory     : 48.2 MB (Beats 8%)
# Link       : https://leetcode.com/problems/rearrange-array-elements-by-sign/
# ==========================================================

class Solution(object):
    def rearrangeArray(self, nums):
        nums_pos = []
        nums_neg = []
        nums_1 = []
        for i in range (0,len(nums)):
            if nums[i] > 0:
                nums_pos.append(nums[i])
            else:
                nums_neg.append(nums[i])

        for i in  range (0,len(nums_pos)):
            nums_1.append(nums_pos[i])
            nums_1.append(nums_neg[i])

        return nums_1
            


        