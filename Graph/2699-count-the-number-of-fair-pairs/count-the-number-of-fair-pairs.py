class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # mp=defaultdict(int)
        nums.sort()
        cnt=0
        for i,ele in enumerate(nums):
            lo,hi=lower-ele,upper-ele
            lft=bisect_left(nums,lo,i+1)
            right=bisect_right(nums,hi,i+1)
            cnt+=right-lft
            # for x in range(lo,hi+1):
            #     if x in mp:
            #         cnt+=mp[x]
            # mp[ele]+=1
                
        return cnt

        