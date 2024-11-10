"""
https://leetcode.com/problems/swim-in-rising-water/description/


"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minh=[(grid[0][0],0,0)]
        vis=set()
        n,m=len(grid),len(grid[0])

        while len(minh)>0:
            h,r,c=heapq.heappop(minh)

            if r==n-1 and c==m-1:
                return h

            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in vis:
                    vis.add((nr,nc))
                    heapq.heappush(minh,(max(h,grid[nr][nc]) ,nr, nc) )   

        return -1
