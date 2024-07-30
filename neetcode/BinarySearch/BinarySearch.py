class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def BS(nums,lo,hi):
            mid=int((lo+hi)/2)
            if lo>hi:
                return -1
            elif(nums[mid]==target):
                return mid
            elif nums[mid]>target:
                return BS(nums,lo,mid-1)
            else:
                return BS(nums,mid+1,hi)
        
        return BS(nums,0,len(nums)-1)