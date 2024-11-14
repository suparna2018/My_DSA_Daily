class Solution:
    def rob(self, num: List[int]) -> int:
        def Calc(nums):
            n=len(nums)
            if n == 0:
                return 0
            elif n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            take=notTake=-1e9
            for ind in range(2,n):
                # take
                
                if ind>1:
                    take=nums[ind]+dp[ind-2]
                # not Take
                notTake=0+dp[ind-1]

                dp[ind]=max(take,notTake)

            return dp[n-1]

        n=len(num)
        if n==0:
            return 0
        elif n==1:
            return num[0]

        takeLast=Calc(num[1:])
       
        takeFirst=Calc(num[:-1])
        return max(takeLast,takeFirst)