
# https://leetcode.com/problems/flood-fill/

from queue import Queue
class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def BFS(x,y,visited):
            n,m=len(grid),len(grid[0])
            q=Queue()
            q.put([x,y])
            visited.add((x,y))
            col=grid[x][y]
            grid[x][y]=color
            while q.qsize():
                x,y=q.get()
                for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx=x+r
                    ny=y+c
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==col and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.put([nx,ny])
                        grid[nx][ny]=color
            return grid
        visited=set()
        return BFS(sr,sc,visited)