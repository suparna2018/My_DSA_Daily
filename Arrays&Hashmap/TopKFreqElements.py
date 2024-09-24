import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        mp={}
        for ele in nums:
            if ele not in mp:
                mp[ele]=1
            else:
                mp[ele]+=1
        for i in range(k):
            max1=max(mp.values())
            for key,value in mp.items():
                if value == max1:
                    maxFreq=key
                    break
            res.append(maxFreq)
            mp.pop(maxFreq)

        return res

def TestCase():
    solution=Solution()
    input=[1,2,2,3,3,3]
    k=2
    output=[[3,2],[2,3]]
    out=solution.topKFrequent(input,k)

    if out in output:
        print("Pass")
    else:
        print("Fail")

if __name__=="__main__":
    TestCase()
