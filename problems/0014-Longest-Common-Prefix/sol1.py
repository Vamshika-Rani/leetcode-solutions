# ==========================================================
# 14. Longest Common Prefix
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.5 MB (Beats 36%)
# Link       : https://leetcode.com/problems/longest-common-prefix/
# ==========================================================

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix