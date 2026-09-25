# ==========================================================
# 1903. Largest Odd Number in String
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 32 ms (Beats 73%)
# Memory     : 17 MB (Beats 64%)
# Link       : https://leetcode.com/problems/largest-odd-number-in-string/
# ==========================================================

class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 != 0:
                return num[:i+1]
            
        return ""
       
        