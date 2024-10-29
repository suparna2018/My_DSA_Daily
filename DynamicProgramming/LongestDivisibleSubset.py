from typing import List

def divisibleSet(arr: List[int]) -> List[int]:
    n=len(arr)
    def solve():
        arr.sort()
        dp=[1]*n
        hash=[ele for ele in range(n)]
        res=[]
        for ind in range(n):
            for prev in range(ind):
                if arr[ind]%arr[prev]==0 and dp[ind]<dp[prev]+1:
                    dp[ind]=dp[prev]+1
                    hash[ind]=prev
        ind=dp.index(max(dp))            
        while(hash[ind]!=ind):
            res.append(arr[ind])
            ind=hash[ind]
        res.append(arr[ind])
        # print(res[::-1])
        return res[::-1]
    ans=solve()
    return ans