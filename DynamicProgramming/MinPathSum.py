
# https://www.naukri.com/code360/problems/minimum-path-sum_985349?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=SUBMISSION

def minCostPath(cost, n, m, x, y):
    def solve(r,c,dp):
        if r==0 and c==0:
            dp[0][0]=cost[r][c]
            return dp[0][0]
        if r<0 or c<0:
            return 1e9
        if dp[r][c]!=-1:
            return dp[r][c]
        up=left=1e9
        # up
        up=cost[r][c]+solve(r-1,c,dp)
        # left
        left=cost[r][c]+solve(r,c-1,dp)
        # diagonal
        diag=cost[r][c]+solve(r-1,c-1,dp)
        dp[r][c]=min(up,left,diag)
        return dp[r][c]

    dp=[[-1]*(m) for _ in range(n)]  
    return solve(x-1,y-1,dp)