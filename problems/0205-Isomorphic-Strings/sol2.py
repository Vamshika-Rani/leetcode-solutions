# ==========================================================
# 205. Isomorphic Strings
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 14 ms (Beats 29%)
# Memory     : 13.5 MB (Beats 63%)
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
        
        