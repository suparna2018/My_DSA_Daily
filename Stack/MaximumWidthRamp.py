"""
https://leetcode.com/problems/maximum-width-ramp/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        maxi = 0
        n = len(nums)
        
        # Step 1: Build the stack with indices in decreasing order of nums values
        for i in range(n):
            if len(stack) == 0 or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Step 2: Iterate from the end and try to maximize the ramp width
        for i in range(n - 1, -1, -1):
            # Pop elements from the stack while the current element can form a ramp with stack's top
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                ind = stack.pop(-1)
                maxi = max(maxi, i - ind)
                
        return maxi