class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        n,m=len(mat),len(mat[0])
        dist=[[-1]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    dist[i][j]=0
                    q.append([i,j])
                else:
                    dist[i][j]=1e9
        # BFS
        while q:
            r,c=q.popleft()
            for dr,dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and dist[nr][nc]>dist[r][c]+1:
                     dist[nr][nc]=dist[r][c]+1
                     q.append([nr,nc])
        return dist