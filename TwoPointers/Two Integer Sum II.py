class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        res=[]
        start=0
        end=n-1
        while start<n:
            print(start,end)
            if start<end:
                if numbers[start]+numbers[end]>target:
                    end-=1
                elif numbers[start]+numbers[end]<target:
                    start+=1
                else:
                    res.append(start+1)
                    res.append(end+1)
                    return res
            
        return res