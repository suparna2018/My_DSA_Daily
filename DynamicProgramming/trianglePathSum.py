# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[]
        for ele in triangle:
            dp+=[[0]*len(ele)]

        dp[n-1]=triangle[n-1]
        next=dp[n-1]
        cur=[]
        for i in range(n-2,-1,-1):
            cur=dp[i]
            for j in range(i,-1,-1):
                down=triangle[i][j]+next[j]   
                diag=triangle[i][j]+next[j+1]
                mini=min(down,diag)
                cur[j]=mini
            next=cur

        return next[0]