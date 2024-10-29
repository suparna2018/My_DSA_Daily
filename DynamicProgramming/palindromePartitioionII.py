"""
https://www.naukri.com/code360/problems/palindrome-partitioning_873266?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=SUBMISSION




"""
def palindromePartitioning(string: str) -> int:
    def solve(i,n):
        if i==n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        miniCOst=1e9
        for j in range(i,n):
            if string[i:j+1]==string[i:j+1][::-1]:
                cost=1+solve(j+1,n)
                miniCOst=min(miniCOst,cost)
                dp[i]=miniCOst

        return dp[i]

    n=len(string)
    dp=[0]*(n+1)
    
    for i in range(n-1,-1,-1):
        miniCOst=1e9
        for j in range(i,n):
            if string[i:j+1]==string[i:j+1][::-1]:
                cost=1+dp[j+1] 
                miniCOst=min(miniCOst,cost)
                dp[i]=miniCOst


    return dp[0]-1