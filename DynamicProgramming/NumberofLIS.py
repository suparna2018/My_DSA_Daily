# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[1]*n
        cnt=[1]*n
        maxi=0
        for ind in range(n):
            for prev in range(ind):
                if arr[ind]>arr[prev] and dp[prev]+1>dp[ind]:
                    dp[ind]=dp[prev]+1  
                    cnt[ind]=cnt[prev]
                elif arr[ind]>arr[prev] and dp[prev]+1==dp[ind]:
                    cnt[ind]+=cnt[prev]

        maxi=max(dp)
        res=0
        print(maxi,dp)
        for i in range(n):
            if dp[i]==maxi:
                res+=cnt[i]  
        return res