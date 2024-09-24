# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def DFS(vis,board,ro,col,n,m):
            vis[ro][col]=1
            for i,j in [[-1,0],[0,-1],[1,0],[0,1]]:
                nro=ro+i
                ncol=col+j
                if 0<=nro<n and 0<=ncol<m:
                    if vis[nro][ncol]==0 and board[nro][ncol]=='O':
                        DFS(vis,board,nro,ncol,n,m)

        n,m= len(board) , len(board[0])
        vis=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i==0 or j==0 or i==n-1 or j==m-1:
                    if vis[i][j]==0 and board[i][j]=='O':
                        DFS(vis,board,i,j,n,m)
        print(vis)
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and board[i][j]=='O':
                    board[i][j]='X'
    


        