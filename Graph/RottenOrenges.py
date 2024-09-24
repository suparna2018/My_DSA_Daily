# https://www.geeksforgeeks.org/problems/rotten-oranges2536/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotten_oranges



from queue import Queue

class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        n=len(grid)
        m=len(grid[0])
        q=Queue()
        vis=[[0]*m for _ in range(n)]
        
#         make the visited
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    vis[i][j]=2
                    q.put([i,j,0])
                    
                elif grid[i][j]==1:
                    vis[i][j]=0
                    
        direction=[(0,1), (1,0), (-1,0), (0,-1)]
        # Do the BFS traversal
        t=0
        maxt=0
        while q.qsize():
           ro, col, t=q.get()
           maxt=max(maxt,t)
           for dr,dc in direction:
               newRo,newCol =ro+dr,col+dc
               if 0 <= newRo < n and 0 <= newCol < m and vis[newRo][newCol] != 2 and grid[newRo][newCol] == 1:
                   q.put([newRo,newCol,t+1])
                   vis[newRo][newCol]=2
                   
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and vis[i][j]!=2:
                    return -1
                    
        return maxt


