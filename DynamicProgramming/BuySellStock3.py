# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/1403247367/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # def solve(ind,buy,cap,dp):
        #     if ind==n or cap==0:
        #         return 0
        #     if dp[ind][buy][cap]!=-1:
        #         return dp[ind][buy][cap]
        #     # buy
        #     if buy==1:
        #         buyOption=-prices[ind]+solve(ind+1,0,cap,dp)
        #         skipOption=0+solve(ind+1,1,cap,dp)
        #         dp[ind][buy][cap] = max(buyOption,skipOption)
        #         return dp[ind][buy][cap]
        #     # noy buy
        #     else:
        #         sellOption=prices[ind]+solve(ind+1,1,cap-1,dp)
        #         stockOption=0+solve(ind+1,0,cap,dp)
        #         dp[ind][buy][cap] = max(sellOption,stockOption)
        #         return dp[ind][buy][cap]

        dp=[ [ [0]*3 for _ in range(2)] for i in range(n+1)]
        
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(3):
                    if buy==1:
                        buyOption=-prices[ind]+dp[ind+1][0][cap]    
                        skipOption=0+dp[ind+1][1][cap]  
                        dp[ind][buy][cap] = max(buyOption,skipOption)
                    else:
                        sellOption=-1e9
                        if cap>0:
                            sellOption=prices[ind]+dp[ind+1][1][cap-1] 
                        stockOption=0+dp[ind+1][0][cap]  
                        dp[ind][buy][cap] = max(sellOption,stockOption)

        return dp[0][1][2]
  