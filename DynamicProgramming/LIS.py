
# https://leetcode.com/problems/longest-increasing-subsequence/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM&status=TO_DO
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(ind,prev,dp):
            if ind==n:
                dp[ind][prev]=0
                return dp[ind][prev]
            if dp[ind][prev]!=-1:
                return dp[ind][prev]
            take=notTake=0
            # not take
            notTake=0+solve(ind+1,prev,dp)
            # take
            if prev==-1 or nums[ind]>nums[prev]:
                take=1+solve(ind+1,ind,dp)

            dp[ind][prev]=max(take,notTake)
            return dp[ind][prev]

        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        return solve(0,-1,dp)   
    

    # tabulation

    # class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n=len(nums)
    #     dp=[[0]*(n+1) for _ in range(n+1)]
    #     for ind in range(n-1,-1,-1):
    #         for prev in range(ind-1,-2,-1):
    #             le=0+dp[ind+1][prev+1] 
    #             # take
    #             if prev==-1 or nums[ind]>nums[prev]:
    #                 le=max(le,1+dp[ind+1][ind+1] )
    #             dp[ind][prev+1]=le
    #     return dp[0][0]