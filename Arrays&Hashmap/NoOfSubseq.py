# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=problem-list-v2&envId=e9snhf4h&status=TO_DO&difficulty=MEDIUM

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort() 
        n=len(nums)
        powers=[1] * n
        res=0
        
        for k in range(1, n):
            powers[k] = (powers[k - 1] * 2) % MOD

        i,j=0,len(nums)-1
        while i<=j:
            if nums[i]+nums[j]<=target:
                
                res+=powers[j-i]% MOD
                i+=1
            else:
                j-=1
        return res 