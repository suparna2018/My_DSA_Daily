
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, values: List[int]) -> int:
        n=len(values)
        # def solve(ind,buy,dp):
        #     if (ind==n):
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
        #     # buy
        #     if buy==1:
        #         buyOption=-values[ind]+solve(ind+1,1-buy,dp)
        #         PassOption= 0+solve(ind+1,buy,dp)
        #         dp[ind][buy]=max(buyOption,PassOption)
            

        #     # not buy
        #     else:
        #         sellOption=values[ind]+solve(ind+1,1-buy,dp)
        #         stockOption=0+solve(ind+1,buy,dp)
        #         dp[ind][buy]=max(sellOption,stockOption )
                
        #     return dp[ind][buy]
            

        dp=[[0]*2 for i in range(n+1)]
        next=[0]*2
        curr=[0]*2
        next[0]=next[1]=0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                # buy
                if buy==1:
                    buyOption=-values[ind]+next[1-buy]   
                    PassOption= 0+next[buy] 
                    curr[buy]=max(buyOption,PassOption)
                

                # not buy
                else:
                    sellOption=values[ind]+next[1-buy]   
                    stockOption=0+next[buy]    
                    curr[buy]=max(sellOption,stockOption )
            next=curr[:]


        return next[1]
