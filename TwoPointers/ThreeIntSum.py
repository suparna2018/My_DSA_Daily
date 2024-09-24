class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start=0
        n=len(nums)
        end=n-1
        ans=set()
        for thirdEle in range(0,n-2):
            start=thirdEle+1
            end=len(nums)-1
            while start<end:
                if nums[start]+nums[end]+nums[thirdEle]==0:
                    # print("ok")
                    ans.add(tuple([nums[thirdEle], nums[start], nums[end]]))
                    while start<end and nums[start]==nums[start+1]:
                        start+=1
                    while start<end and nums[end]==nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
                elif nums[start]+nums[end]+nums[thirdEle]<0:
                    start+=1
                else:
                    end-=1
        answer=[]
        for ele in ans:
            answer.append(list(ele))
        return answer