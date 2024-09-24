# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n):
            if n==0:
                return 1
            lh=rh=0
            # left
            lh=solve(n-1)
            # right
            if n>1:
                rh=solve(n-2)
            return rh+lh
        prev=prev2prev=1
        curr=1
        for i in range(2,n+1):
            curr=prev+prev2prev
            prev2prev=prev
            prev=curr
        return curr