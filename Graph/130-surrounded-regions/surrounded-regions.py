class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m=len(board),len(board[0])
        vis=set()
        
        def DFS(vis,row,col):
            vis.add((row,col))
            for dr,dc in [(0,-1),(-1,0) ,(1,0),(0,1)]:
                nr,nc=row+dr,col+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in vis and board[nr][nc]=='O':
                    DFS(vis,nr,nc)

        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if (i,j) not in vis and board[i][j]=='O':
                        DFS(vis,i,j) 

        for i in range(n):
            for j in range(m):
                if (i,j) not in vis and board[i][j]=='O':
                    board[i][j]='X'