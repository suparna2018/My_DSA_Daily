from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lft=[1]*len(nums)
        right=[1]*len(nums)
        prod=[1]*len(nums)
        for i in range(1,len(nums)):
            lft[i]=lft[i-1]*nums[i-1]
        for i in reversed(range(len(nums)-1)):
            right[i]=right[i+1]*nums[i+1]
        for i in range(0,len(nums)):
            prod[i]=lft[i]*right[i]
        return prod
    
def testCase():
    solution=Solution()
    input=[1,2,4,6]
    expectedOutput=[48,24,12,8]
    result=solution.productExceptSelf(input)
    if result==expectedOutput:
        print("Passed")
    else:
        print("failed")

if __name__== "__main__":
    testCase()


        
# TC: O(n)
# SC: O(n)   