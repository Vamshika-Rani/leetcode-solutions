# ==========================================================
# 1295. Find Numbers with Even Number of Digits
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 2 ms (Beats 61%)
# Memory     : 12.1 MB (Beats 100%)
# Link       : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# ==========================================================

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num))%2 == 0: 
                count = count + 1
        return count