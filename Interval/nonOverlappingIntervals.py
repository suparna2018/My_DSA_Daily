# https://neetcode.io/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals , key=lambda intervals:intervals[1])
        cnt=1
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if end<=intervals[i][0]:
                end=intervals[i][1]
                cnt+=1
        # print(intervals)
        return len(intervals)-cnt
    