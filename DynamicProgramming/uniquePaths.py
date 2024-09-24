# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:    
        dp=[[0]*n for _ in range(m)]
        cur=dp[0]
        prev=dp[0]
        for i in range(m):
            cur=dp[i]
            for j in range(n):
                if i==0 and j==0:
                    cur[j]=1
                else:
                    up=left=0
                    # up
                    up+=prev[j]        
                    # left
                    left+=cur[j-1]
                    cur[j]=up+left
            prev=cur    

        return prev[n-1]  