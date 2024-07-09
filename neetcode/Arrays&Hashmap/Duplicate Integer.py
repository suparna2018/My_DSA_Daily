from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st={}
        for ele in nums:
            if ele not in st:
                st[ele]=1
            else:
                st[ele]+=1
        for ele in st:
            if st[ele]>1:
                print(ele)
                return True
        return False
def testCase():
    solution=Solution()
    input=[1,2,3,3]
    result=solution.hasDuplicate(input)
    if result==True:
        print("Pass")
    else:
        print("Fail")
    