# ==========================================================
# 189. Rotate Array
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 173 ms (Beats 13%)
# Memory     : 26.7 MB (Beats 77%)
# Link       : https://leetcode.com/problems/rotate-array/
# ==========================================================

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return

        k = k % n

        l = 0
        r = n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = 0
        r = k-1
        m = k
        n = len(nums)-1
        while(l<=r):
            nums[l],nums[r] = nums[r],nums[l]
            l = l+1
            r = r-1
        while(m<=n):
            nums[m],nums[n] = nums[n],nums[m]
            m = m+1
            n = n-1

        return nums

            


        