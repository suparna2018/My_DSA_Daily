import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles,h,k):
            hours=0
            for ele in piles:
                hours+=math.ceil(ele/k)
            return hours<=h

        left,right=1,max(piles)
        while left<right:
            mid=(left+right)//2
            if canFinish(piles,h,mid):
                right=mid
            else:
                left=mid+1
        return left        