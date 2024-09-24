# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp=[[0]*m for _ in range(n)]
        dp[n-1]=matrix[n-1]
        for i in range(n-2,-1,-1):
            for j in range(m-1,-1,-1):
                # up
                up=matrix[i][j]+dp[i+1][j]
                # down left
                if j>0:
                    dl=matrix[i][j]+dp[i+1][j-1]
                else:
                    dl=1e9
                # down right
                if j+1<m:
                    dr=matrix[i][j]+dp[i+1][j+1]
                else:
                    dr=1e9
                dp[i][j]=min(up,min(dl,dr))
        return min(dp[0])