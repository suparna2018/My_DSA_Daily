"""
Problem statement
A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 10^2
1<= wi <= 50
1 <= vi <= 10^2
1 <= W <= 10^3

Time Limit: 1 second
Sample Input:
1 
4
1 2 4 5
5 4 8 6
5
Sample Output:
13
"""


from os import *
from sys import *
from collections import *
from math import *

## Print output as specified in the question.
def Knapsack(N,W,V,Bag):
    # def solve(ind,target,dp):
    #     if ind==0:
    #         if (W[0]<=target):
    #             return V[0]
    #         return 0

    #     if(dp[ind][target]!=-1):
    #         return dp[ind][target]

    #     # pick
    #     take=-1e9
    #     if(W[ind]<=target):
    #          take=V[ind]+solve(ind-1,target-W[ind],dp)
    #     # not pick
    #     notTake=0+solve(ind-1,target,dp)

    #     dp[ind][target]=max(take,notTake)
        
    #     return dp[ind][target]

    # dp=[[0]*(Bag+1) for _ in range(N)]
    prev=[0]*(Bag+1)
    curr=[0]*(Bag+1)
    for ind in range(W[0],Bag+1):
        prev[ind]=V[0]

    for ind in range(1,N):
        for target in range(Bag+1):
            # pick
            take=-1e9
            if(W[ind]<=target):
                take=V[ind]+prev[target-W[ind]]    
            # not pick
            notTake=0+prev[target]    

            curr[target]=max(take,notTake)
            
        prev=curr.copy()
        
    return prev[Bag]      


## Read input as specified in the question.
T=int(input())
for _ in range(T):
    N=int(input())
    W=list(map(int,input().split()))
    V=list(map(int,input().split()))
    Bag=int(input())
    res=Knapsack(N,W,V,Bag)
    print(res)