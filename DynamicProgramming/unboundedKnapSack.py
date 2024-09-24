"""
Problem statement
You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.



You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed to take one item multiple times.



Example:
Input: 
'n' = 3, 'w' = 10, 
'profit' = [5, 11, 13]
'weight' = [2, 4, 6]

Output: 27

Explanation:
We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 = 11 + 11 + 5 = 27. Therefore maximum profit = 27.
"""

from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    def solve(ind,target):
        if ind==0:
            # if(target>=weight[0]):
            return (target//weight[0])*profit[0]

        if(dp[ind][target]!=-1):
            return dp[ind][target]

        take=-1e9
        # take
        if(target>=weight[ind]):
            take=profit[ind]+solve(ind,target-weight[ind])
        # not take
        notTake=0+solve(ind-1,target)
        dp[ind][target]=max(take,notTake)
        
        return dp[ind][target]

    dp=[[-1]*(w+1) for _ in range(n)]
    return solve(n-1,w)