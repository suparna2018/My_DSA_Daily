# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

#User function Template for python3
class Solution:
    def isSubsetSum (self, N, arr, sum):
        def solve(ind,target,dp):
            if target==0:
                dp[ind][target]=True
                return True
                
            elif ind==0:
                dp[ind][target]=(arr[0]==target)
                return dp[ind][target]
            
            if dp[ind][target]!=-1:
                return dp[ind][target]
                
            notTake=solve(ind-1,target,dp)
            Take=False
            
            if arr[ind]<=target:
                Take=solve(ind-1,target-arr[ind],dp)
                
            dp[ind][target]=notTake or Take
            return dp[ind][target]
            
        dp=[[-1]*(sum+1) for i in range(N)]
        return solve(N-1,sum,dp)
        
        