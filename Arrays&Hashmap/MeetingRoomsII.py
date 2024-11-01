"""
https://leetcode.com/problems/meeting-rooms-ii/description/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM%2CHARD
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap=[]
        for i in intervals:
            if heap and heap[0]<=i[0]:
                heapq.heapreplace(heap,i[1])
            else:
                heapq.heappush(heap,i[1])
                
        return len(heap) 
