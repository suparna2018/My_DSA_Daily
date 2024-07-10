from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        mp={}
        for i in range(len(nums)):
            if target-nums[i] not in mp:
                mp[nums[i]]=i
            else:
                res.append(i)
                res.append(mp[target-nums[i]])
        return sorted(res)

def TestCase():
    solution=Solution()

    input=[3,4,5,6]
    target=11
    output=[2,3]
    res=solution.twoSum(input,target)
    if res==output:
        print("Pass")
    else:
        print(res)
        print("Fail")
    
    return

if __name__=="__main__":
    TestCase()
