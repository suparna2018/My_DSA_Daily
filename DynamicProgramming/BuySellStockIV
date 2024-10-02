# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # def solve(ind,buy,dp):
        #     if ind>=n :
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
        #     # buy
        #     if(buy==1):
        #         buyOption=-prices[ind]+solve(ind+1,0,dp)
        #         skipOption=0+solve(ind+1,1,dp)
        #         dp[ind][buy]=max(buyOption,skipOption)
               
        #     # not buy
        #     else:
        #         sellOption=prices[ind]+solve(ind+2,1,dp)
        #         stockOption=0+solve(ind+1,0,dp)
        #         dp[ind][buy]= max(sellOption,stockOption)

        #     return dp[ind][buy] 

        # dp=[[0]*(2) for _ in range(n+2)]
        front2=[0]*(2)
        front1=[0]*(2)
        curr=[0]*(2)

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                # buy
                if(buy==1):
                    buyOption=-prices[ind]+front1[0] 
                    skipOption=0+front1[1]   
                    curr[buy]=max(buyOption,skipOption)
                
                # not buy
                else:
                    sellOption=prices[ind]+front2[1] 
                    stockOption=0+front1[0]  
                    curr[buy]= max(sellOption,stockOption)
            
            front2=front1[:]
            front1=curr[:]

        return curr[1] 
