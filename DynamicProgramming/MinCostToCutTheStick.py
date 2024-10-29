
# https://www.naukri.com/code360/problems/cost-to-cut-a-chocolate_3208460?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

from typing import List

# Memoization
def cost(n: int, c: int, cut: List[int]) -> int:
    def solve(i,j,cuts,dp):
        if i>j: 
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini=1e9
        for k in range(i,j+1):
            steps=cuts[j+1]-cuts[i-1]+solve(i,k-1,cuts,dp)+solve(k+1,j,cuts,dp)
            mini=min(mini,steps)
        dp[i][j]=mini
        return mini
    cut.append(0)
    cut.append(n)
    cuts=sorted(cut)
    dp=[[-1]*n for _ in range(n)]
    return solve(1,c,cuts,dp)


# Tabulation


def cost(n: int, c: int, cuts: List[int]) -> int:    
    # Extend the cuts list with 0 and n, and sort it
    cuts = [0] + cuts + [n]
    cuts.sort()
    
    # Create a 2D DP table initialized with zeros
    dp = [[0] * (c + 2) for _ in range(c + 2)]

    # Calculate the minimum cost using dynamic programming
    for i in range(c, 0, -1):
        for j in range(1, c + 1):
            if i > j:
                continue
            
            mini = float('inf')
            
            for ind in range(i, j + 1):
                ans = cuts[j + 1] - cuts[i - 1] + dp[i][ind - 1] + dp[ind + 1][j]
                mini = min(mini, ans)
            
            dp[i][j] = mini
    
    return dp[1][c]