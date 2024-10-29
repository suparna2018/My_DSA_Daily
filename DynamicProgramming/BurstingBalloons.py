# https://www.naukri.com/code360/problems/mining-diamonds_4244494?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=PROBLEM


# Memoization
from os import *
from sys import *
from collections import *
from math import *

from typing import List

def maxCoins(a: List[int]) -> int:
    def solve(i,j,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini=-1e9
        for k in range(i,j+1):
            cost=a[j+1]*a[k]*a[i-1]+solve(i,k-1,dp)+solve(k+1,j,dp)
            mini=max(mini,cost)
        dp[i][j]=mini
        return mini
    n=len(a)
    a=[1]+a+[1]
    sorted(a)
    dp=[[-1]*(n+2) for _ in range(n+2)]
    return solve(1,n,dp)

# Tabulattion

def maxCoins(a: List[int]) -> int:
    n = len(a)
    
    # Extend the list 'a' with 1s at both ends
    a.insert(0, 1)
    a.append(1)

    # Create a 2D DP table initialized with 0s
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # Loop from the end of 'a' to the beginning
    for i in range(n, 0, -1):
        for j in range(1, n + 1):
            if i > j:
                continue
            maxi = float('-inf')
            
            # Iterate through the balloons from 'i' to 'j'
            for ind in range(i, j + 1):
                cost = a[i - 1] * a[ind] * a[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                maxi = max(maxi, cost)
            
            dp[i][j] = maxi
    
    return dp[1][n]