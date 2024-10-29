# https://leetcode.com/problems/number-of-islands/

class Solution:
    def __init__(self):
        self.dirRo=[0,1,0,-1]
        self.dirCol=[1,0,-1,0]
    def dfs(self,r,c,n,m,grid,vis):
        if(r>=n or r<0 or c>=m or c<0):
            return
        vis[r][c]=1
        for i in range(4):
            row=r+self.dirRo[i]
            col=c+self.dirCol[i]
            if(0<=row<n and 0<=col<m and grid[row][col]=='1' and vis[row][col]==0):
                self.dfs(row,col,n,m,grid,vis)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        vis=[[0 for j in range(m) ]for i in range(n)]
        for i in range(n):
            for j in range(m):
                if(vis[i][j]==0 and grid[i][j]=='1'):
                    ans+=1
                    self.dfs(i,j,n,m,grid,vis)
        return ans
