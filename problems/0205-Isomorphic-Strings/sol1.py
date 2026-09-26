# ==========================================================
# 205. Isomorphic Strings
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 11 ms (Beats 58%)
# Memory     : 13.3 MB (Beats 92%)
# Link       : https://leetcode.com/problems/isomorphic-strings/
# ==========================================================

class Solution(object):
    def isIsomorphic(self, s, t):
        mapping = {}
        reverse_mapping = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):

            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]

            if t[i] in reverse_mapping:
                if reverse_mapping[t[i]] != s[i]:
                    return False
            else:
                reverse_mapping[t[i]] = s[i]

        return True
        
        