class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        ans=n+1
        for i in range(n):
            if nums[i]>n or nums[i]<=0:
                nums[i]=n+1
           
        for i in range(n):
            val=abs(nums[i])
            if val<=n:
                if nums[val-1]>0:
                    nums[val-1]=nums[val-1]*(-1)

        print(nums)
        for i in range(n):
            if nums[i]>0:
                ans=i+1
                break

        return ans