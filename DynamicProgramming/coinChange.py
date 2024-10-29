# https://leetcode.com/problems/coin-change/description/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM&status=TO_DO

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(ind,target,dp):
            if target==0:return 0
            if target<0:return 1e9
            if ind<0:return 1e9

            if dp[ind][target]!=-1:
                return dp[ind][target]
            # take
            take=1e9
            if coins[ind]<=target:
                take=1+solve(ind,target-coins[ind],dp)
            # not Take
            notTake=0+solve(ind-1,target,dp)

            dp[ind][target]=min(take,notTake)

            return dp[ind][target]

        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for target in range(amount+1):
            if target%coins[0]==0:
                dp[0][target]=target//coins[0]
            else:
                dp[0][target]=1e9

        for ind in range(1,n):
            for target in range(amount+1):
                # take
                take=1e9
                if coins[ind]<=target:
                    take=1+dp[ind][target-coins[ind]]
                # not Take
                notTake=0+dp[ind-1][target]
                dp[ind][target]=min(take,notTake)

        res=dp[n-1][amount] 
        return res if res!=1e9 else -1     