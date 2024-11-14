class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis=set()
        n,m=len(grid),len(grid[0])
        fresh=0
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1

        if fresh==0:
            return 0
        # BFS
        maxt=0
        while len(q)>0:
            r,c,t=q.popleft()
            maxt=max(maxt,t)
            for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in vis:
                    vis.add((nr,nc))
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc,t+1))
                        fresh-=1

        if fresh>0:
            return -1
        
        return maxt