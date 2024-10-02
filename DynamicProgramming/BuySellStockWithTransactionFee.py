# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    buyOption=-prices[ind]-fee+dp[ind+1][1-buy]
                    skipOption=0+dp[ind+1][buy]
                    dp[ind][buy]=max(skipOption,buyOption)
                else:
                    sellOption=prices[ind]+dp[ind+1][1-buy]
                    stockOption=0+dp[ind+1][buy]
                    dp[ind][buy]=max(sellOption,stockOption)

        return dp[0][1]