""""
https://leetcode.com/problems/jump-game-ii/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        def solve(ind,dp):
            if ind>=n-1:
                return 0

            if dp[ind]!=-1:
                return dp[ind]
            i=1
            maxJump=nums[ind]
            minJumps=1e9
            while i<=maxJump:
                if ind+i<n:
                    minJumps=min(minJumps, 1+solve(ind+i,dp))
                i+=1

            dp[ind]=minJumps
            return dp[ind]

        n=len(nums)
        dp=[0]*(n+1)

        for ind in range(n-2,-1,-1):
            i=1
            maxJump=nums[ind]
            minJumps=1e9
            while i<=maxJump:
                if ind+i<n:
                    minJumps=min(minJumps, 1+dp[ind+i])
                i+=1
            dp[ind]=minJumps

        return dp[0]