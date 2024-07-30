class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(nums,lo,hi):
            while lo<=hi:
                mid=(lo+hi)//2
                if nums[mid]==target:
                    return mid
                # if left part is sorted
                if nums[mid]>=nums[lo]:
                    if nums[lo]<=target<=nums[mid]:
                        hi=mid-1
                    else:
                        lo=mid+1
                # if right part is sorted
                else:
                    if nums[mid]<=target<=nums[hi]:
                        lo=mid+1
                        
                    else:
                        hi=mid-1
            return -1
        return BS(nums,0,len(nums)-1)
        

