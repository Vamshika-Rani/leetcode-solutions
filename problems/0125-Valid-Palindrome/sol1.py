# ==========================================================
# 125. Valid Palindrome
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 133 ms (Beats 27%)
# Memory     : 13.1 MB (Beats 39%)
# Link       : https://leetcode.com/problems/valid-palindrome/
# ==========================================================

class Solution(object):
    def isPalindrome(self, s):
        string =""
        for ch in s:
            if ch.isalnum():
                string = string + ch
        
        string = string.lower()
        if string[::-1] == string:
            return True
        else:
            return False

        