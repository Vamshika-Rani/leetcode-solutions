# ==========================================================
# 73. Set Matrix Zeroes
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 518 ms (Beats 8%)
# Memory     : 13.6 MB (Beats 96%)
# Link       : https://leetcode.com/problems/set-matrix-zeroes/
# ==========================================================

class Solution(object):
    def setZeroes(self, matrix):
        rows = []
        cols = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            for j in range (0,len(matrix[0])):
                matrix[i][j] = 0
        for j in cols:
            for i in range (0,len(matrix)):
                matrix[i][j] = 0

        return matrix
        
        