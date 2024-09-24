class Solution:
    def findMin(self, nums: List[int]) -> int:
        def BS(nums,lo,hi):
            ans=float('inf')
            while(lo<=hi):
                mid=(lo+hi)//2
                if nums[lo]<=nums[mid]:
                    ans=min(ans,nums[lo])
                    lo=mid+1
                else:
                    ans=min(ans,nums[mid])
                    hi=mid-1
            return ans
        return BS(nums,0,len(nums)-1)