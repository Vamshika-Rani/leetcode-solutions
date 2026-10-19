# ==========================================================
# 202. Happy Number
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 2 ms (Beats 56%)
# Memory     : 12 MB (Beats 99%)
# Link       : https://leetcode.com/problems/happy-number/
# ==========================================================

class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            total = 0
            while n > 0:
                rem = n % 10
                total += rem * rem
                n = n // 10

            n = total

        return True
        