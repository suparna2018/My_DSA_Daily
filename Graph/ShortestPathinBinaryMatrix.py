# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from queue import Queue

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q=Queue()
        q.put([0,0])
        n,m=len(grid),len(grid[0])
        vis=[[0]*m for _ in range(n)]
        dist=[[1e9]*m for _ in range(n)]
        if grid[0][0]==1 or grid[n-1][m-1]:
            return -1

        vis[0][0]=1
        dist[0][0]=1
        direction=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

        while not q.empty():
            x,y=q.get()
            for dx,dy in direction:
                newx,newy=x+dx,y+dy
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]):
                    if vis[newx][newy]==0 and grid[newx][newy]==0:
                        if dist[newx][newy]>dist[x][y]+1:
                            dist[newx][newy]=dist[x][y]+1
                            q.put([newx,newy])
        print(dist)
        return dist[n-1][m-1] if dist[n-1][m-1]!=1e9 else -1