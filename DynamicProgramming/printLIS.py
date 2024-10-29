
class Solution:
    def printLIS(self,arr,n):
        dp=[1]*n
        res=[]
        hash=[ele for ele in range(n)]
        for ind in range(n):
            for prev in range(0,ind):
                if(arr[prev]<arr[ind] and dp[ind]<dp[prev]+1):
                    dp[ind]=1+dp[prev]
                    hash[ind]=prev
        print(max(dp))
        ind=dp.index(max(dp))
        while(hash[ind]!=ind):
            res.append(str(arr[ind]))
            ind=hash[ind]
        res.append(str(arr[ind]))
        print(res[::-1])
        return max(dp),res[::-1]
    
arr=[5,4,11,1,16,7,8,9]

solution=Solution()
solution.printLIS(arr,len(arr))