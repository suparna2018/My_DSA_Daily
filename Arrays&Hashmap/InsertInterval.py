# https://leetcode.com/problems/insert-interval/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM&status=TO_DO

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        currInterval=newInterval
        if len(intervals)==0:
            return [newInterval]
        ans=[]
        ind=len(intervals)
        for i in range(len(intervals)):
            if intervals[i][1]<currInterval[0]:
                ans.append(intervals[i])
            elif intervals[i][0]>currInterval[1]:
                ind=i
                print(i)
                break
            else:
                currInterval=[min(intervals[i][0],currInterval[0]),max(intervals[i][1],currInterval[1])]
        
        ans.append(currInterval)
        ans+=intervals[ind:]
        return ans
