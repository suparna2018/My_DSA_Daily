# https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1
from typing import List

class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        def LIS(nums):
            dp=[1]*n
            for ind in range(n):
                for prev in range(ind):
                    if nums[prev]<nums[ind] and dp[ind]<dp[prev]+1:
                        dp[ind]=dp[prev]+1
            return dp
        dp1=LIS(nums)
        dp2=LIS(nums[::-1])[::-1]
        # print(dp1,dp2)
        for i in range(n):
            if dp1[i]>1 and dp2[i]>1:
                dp1[i]=dp1[i]+dp2[i]
            else:
                dp1[i]=0
       
        return max(dp1)-1 if max(dp1)>1 else 0