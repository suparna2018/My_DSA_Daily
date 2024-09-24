# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0]*m for _ in range(n)]
        prev=dp[0]
        for i in range(n):
            cur=dp[i]
            for j in range(m):
                if i==0 and j==0:
                    cur[j]=grid[0][0]
                else:
                    up=left=0
                    # up
                    if i>0:
                        up=grid[i][j]+prev[j]
                    else:
                        up=1e9
                    # left
                    if j>0:
                        left=grid[i][j]+cur[j-1]
                    else:
                        left=1e9

                    cur[j]=min(up,left)
            prev=cur

        return prev[m-1]