class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans=-1e9
        n=len(arr1)
        for p1 in [-1,1]:
            for p2 in [-1,1]:
                for p3 in [-1,1]:
                    maxVal=-1e9
                    minVal=1e9
                    for i in range(n):
                        val=p1*arr1[i]+p2*arr2[i]+p3*i
                        maxVal=max(maxVal,val)
                        minVal=min(minVal,val)

                    ans=max(ans,maxVal-minVal)
        return ans