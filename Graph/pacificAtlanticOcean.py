"""
https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=problem-list-v2&envId=oizxjoit&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

# -------------------------------------------------------------BFS--------------------------------------------------------------------------

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return
        n,m=len(heights),len(heights[0])
        # Create visited matrices for both oceans
        pacificVis=set()
        atlanticVis=set()
        # Create queue for both oceans
        pacificQ=deque()
        atlanticQ=deque()
        # Add cells in the first and last rows to their respective queues
        for col in range(m):
            pacificVis.add((0,col))
            atlanticVis.add((n-1,col))
            pacificQ.append((0,col))
            atlanticQ.append((n-1,col))
        # Add cells in the first and last columns to their respective queues
        for row in range(n):
            pacificVis.add((row,0))
            atlanticVis.add((row,m-1))
            pacificQ.append((row,0))
            atlanticQ.append((row,m-1))
        # Define helper function to check if a cell can flow to an ocean
        def bfs(Q,vis):
            while Q:
                ro,col=Q.popleft()
                # Check adjacent cells
                for dr,dc in [(0,-1),(0,1),(1,0),(-1,0)]:
                    dro,dcol=ro+dr,col+dc
                    # Check if cell is within bounds and hasn't been visited yet
                    if 0<=dro<n and 0<=dcol<m and (dro,dcol) not in vis:
                        # Check if cell can flow to the ocean
                        if heights[dro][dcol]>=heights[ro][col]:
                            vis.add((dro,dcol))
                            Q.append((dro,dcol))
                        

        # Run BFS on both oceans starting from the boundary cells
        bfs(pacificQ,pacificVis)
        bfs(atlanticQ,atlanticVis)
        # Find the cells that can flow to both oceans
        res=[list(cells) for cells in pacificVis & atlanticVis]
        return res
        
# ----------------------------------------------------------DFS--------------------------------------------------------------------------------------------

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVis,atlanticVis=set(), set()
        n,m=len(heights),len(heights[0])

        def dfs(vis,row,col,H):
            if row < 0 or row >= n or col < 0 or col >= m:
                return
            if (row,col) in vis:
                return

            if heights[row][col]<H:
                return

            vis.add((row,col))
            
            dfs(vis,row-1,col,heights[row][col])
            dfs(vis,row,col-1,heights[row][col])
            dfs(vis,row+1,col,heights[row][col])
            dfs(vis,row,col+1,heights[row][col])

        for col in range(m):
            dfs(pacificVis,0,col,heights[0][col])
            dfs(atlanticVis,n-1,col,heights[n-1][col])

        for row in range(n):
            dfs(pacificVis,row,0,heights[row][0])
            dfs(atlanticVis,row,m-1,heights[row][m-1])

        res=[list(cell) for cell in pacificVis & atlanticVis]
        return res

