"""
https://leetcode.com/problems/find-median-from-data-stream/description/?envType=problem-list-v2&envId=oizxjoit&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        if len(self.small)==len(self.large):
            heappush(self.large,-heappushpop(self.small,-num))
        else:
            heappush(self.small,-heappushpop(self.large,num))

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return float(self.large[0]-self.small[0])/2.0
        else:
            return float(self.large[0])
