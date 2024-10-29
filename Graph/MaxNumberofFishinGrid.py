# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/

from queue import Queue

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.ans=0
        def BFS(i,j,sum):
            q.put([i,j])
            vis[i][j]=1
            sum+=grid[i][j] 
            while q.qsize()>0:
                x,y=q.get()   
                for dx,dy in direction:
                    newx,newy=x+dx,y+dy
                    if 0<=newx<n and 0<=newy<m:
                        if vis[newx][newy]==0 and grid[newx][newy]>0:
                            sum+=grid[newx][newy]
                            vis[newx][newy]=1
                            q.put([newx,newy])        
            return sum

        q=Queue()
        maxVal=-1e9
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        n,m=len(grid),len(grid[0])
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0 and vis[i][j]==0:
                    print(i,j)
                    maxVal=max(BFS(i,j,0),maxVal)
        print(vis)

        return maxVal if maxVal!=-1e9 else 0
                    