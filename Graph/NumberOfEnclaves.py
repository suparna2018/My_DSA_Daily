# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(vis,grid,ro,col,n,m):
            vis[ro][col]=1
            for i,j in [(1,0),(0,1),(0,-1),(-1,0)]:
                nro=ro+i
                ncol=col+j
                if 0<=nro<n and 0<=ncol<m:
                    if vis[nro][ncol]==0 and grid[nro][ncol]==1:
                        dfs(vis,grid,nro,ncol,n,m)
                        
        cnt=0
        n,m = len(grid) , len(grid[0])
        vis=[[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0 or i==n-1 or j==m-1:
                    if vis[i][j]==0 and grid[i][j]==1:
                        dfs(vis,grid,i,j,n,m)
            else:
                pass

        print(vis)        
        print("")
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]==1:
                    cnt+=1
        return cnt