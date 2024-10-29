

# https://leetcode.com/problems/as-far-from-land-as-possible/


from queue import Queue 
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        q=Queue()
        dist=[[1e9]*n]
        vis=[[0]*m for _ in range(n)]
        res=-1e9
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.put([i,j,0])
                    vis[i][j]=1

        while q.qsize()>0:
            i,j,dist=q.get()
            for dx,dy in directions:
                newx=i+dx
                newy=j+dy
                if 0<=newx<n and 0<=newy<m and  vis[newx][newy]==0:
                    maxVal=dist+1
                    res=max(res,maxVal)
                    q.put([newx,newy,maxVal])
                    vis[newx][newy]=1