# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, arr: List[int]) -> int:
        def solve(ind,dp,start,end):
            dp[start]=arr[start]
            take=notTake=-1e9
            print(start,end)
            for ind in range(start,end+1):
                # take
                if ind>1:
                    take=nums[ind]+dp[ind-2]
                # not Take
                notTake=0+dp[ind-1]
                dp[ind]=max(take,notTake)
            return dp[ind]

        if len(arr)==1:
            return arr[0]
        elif len(arr)==2:
            return max(arr)

        n=len(arr)
        dp=[0]*(len(arr)-1)
        nums=arr[:-1]
        takefirst=solve(len(nums)-1,dp,0,n-2)  
        dp=[0]*(len(arr)-1)
        nums=arr[1:]
        takelast=solve(len(nums)-1,dp,1,n-1)
        return max(takefirst,takelast)