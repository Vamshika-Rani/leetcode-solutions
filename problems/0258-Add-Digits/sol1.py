# ==========================================================
# 258. Add Digits
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 2 ms (Beats 27%)
# Memory     : 12.2 MB (Beats 98%)
# Link       : https://leetcode.com/problems/add-digits/
# ==========================================================

class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            sum = 0
            while num > 0:
                rem = num % 10
                sum = sum + rem
                num = num // 10
            num = sum
        return num

        