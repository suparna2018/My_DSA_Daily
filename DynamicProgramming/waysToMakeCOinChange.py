"""
Problem statement
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}. You need to figure out the total number of ways W, in which you can make a change for value V using coins of denominations from D. Print 0, if a change isn't possible.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3
1 2 3
4
Sample Output 1:
4
Explanation for Sample Output 1:
We can make a change for the value V = 4 in four ways.
1. (1,1,1,1), 
2. (1,1, 2), [One thing to note here is, (1, 1, 2) is same as that of (2, 1, 1) and (1, 2, 1)]
3. (1, 3), and 
4. (2, 2)
Sample Input 2 :
3
5 3 2
1
Sample Output 2:
0
    
    """

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def countWaysToMakeChange(arr, value) :
    # def solve(ind,total,dp):
    #     if ind==0:
    #         return (total%arr[ind])==0
    #     # take
    #     if(dp[ind][total]!=-1):
    #         return dp[ind][total]

    #     take=0
    #     if arr[ind]<=total:
    #         take=solve(ind,total-arr[ind],dp)
    #     # not take
    #     notTake=solve(ind-1,total,dp)
    #     dp[ind][total]=take+notTake
    #     return dp[ind][total]
    # dp=[[-1]*(value+1) for _ in range(len(arr))]
    # return solve(len(arr)-1,value,dp)
    def solve():
        dp=[[0]*(value+1) for _ in range(len(arr))]
        for v in range(value+1):
            if (v%arr[0])==0:
                dp[0][v]=1
            else:
                dp[0][v]=0


        for ind in range(1,len(arr)):
            for target in range(value+1):
                take=0
                if arr[ind]<=target:
                    take=dp[ind][target-arr[ind]]
                nonTake=dp[ind-1][target]

                dp[ind][target]=take+nonTake
        return dp[len(arr)-1][value]
    return solve()