class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable=0
        n=len(nums)
        for i in range(n):
            if i >reachable:
                return False
            reachable=max(nums[i]+i,reachable)
            if reachable>=n-1:
                return True

        return False

        