# https://leetcode.com/problems/unique-paths-ii/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # def solve(i,j,dp):
        #     if obstacleGrid[i][j]==1:
        #         return 0
        #     elif i==0 and j==0:
        #         dp[i][j]=1
        #         return dp[i][j]
        #     elif i<0 or j<0:
        #         return 0
        #     elif dp[i][j]!=-1:
        #         return dp[i][j]
        #     up=left=0
        #     # up
        #     up+=solve(i-1,j,dp)
        #     # left
        #     left+=solve(i,j-1,dp)
        #     dp[i][j]=up+left
        #     return dp[i][j]
        n=len(obstacleGrid)  
        m=len(obstacleGrid[0])
        dp=[[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=left=0
                    # up
                    up+=dp[i-1][j] 
                    # left
                    left+=dp[i][j-1]
                    dp[i][j]=up+left
                
        return dp[n-1][m-1]