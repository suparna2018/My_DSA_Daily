"""
https://www.naukri.com/code360/problems/partition-array-for-maximum-sum_3755255?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

"""

from typing import List

def maximumSubarray(arr: List[int], k: int) -> int:
    def solve(ind):
        if ind==n:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        maxi=-1e9
        length=0
        maxSum=-1e9
        for j in range(ind,min(ind+k,n)):
            length+=1
            maxi=max(maxi,arr[j])
            sum=maxi*length+solve(j+1)
            maxSum=max(maxSum,sum)
            dp[ind]=maxSum

        return dp[ind]
    n=len(arr)
    dp=[0]*(n+1)
    for ind in range(n-1,-1,-1):
        maxi=-1e9
        length=0
        maxSum=-1e9
        for j in range(ind,min(ind+k,n)):
            length+=1
            maxi=max(maxi,arr[j])
            sum=maxi*length+dp[j+1] 
            maxSum=max(maxSum,sum)
            dp[ind]=maxSum

    return dp[0]