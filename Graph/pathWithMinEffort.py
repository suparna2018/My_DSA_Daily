# https://leetcode.com/problems/path-with-minimum-effort/description/


import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m=len(heights),len(heights[0])
        q=[]
        heapq.heappush(q,[0,0,0])
        dist=[[1e9]*m for _ in range(n)]
        dist[0][0]=0
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        while q:
            effort,x,y=heapq.heappop(q)
            for dx,dy in directions:
                newx=x+dx
                newy=y+dy
                if 0<=newx<n and 0<=newy<m:
                    newdist=max(abs(heights[newx][newy]-heights[x][y]),effort)
                    if newdist<dist[newx][newy]:
                        dist[newx][newy]=newdist
                        heapq.heappush(q,[newdist,newx,newy])
        return dist[n-1][m-1]