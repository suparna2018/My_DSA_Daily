from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        maxLen=0
        for num in nums:
            currLen=0
            if num-1 not in st:
                cuurNum=num
                currLen=1
            while num+1 in st:
                num=num+1
                currLen+=1
            maxLen=max(maxLen,currLen)
        return maxLen

def TestCase():
    solution=Solution()
    input=[2,20,4,10,3,4,5]
    output=4
    res=solution.longestConsecutive(input)
    if res==output:
        print("Pass")
    else:
        print("Fail")

if __name__=="__main__":
    TestCase()