"""
https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-ele for ele in nums]
        heapq.heapify(nums)
        totalVal=0
        for i in range(k):
            currVal=heapq.heappop(nums)
            totalVal+=currVal
            
            calcVal=-math.ceil(-currVal/3)
            heapq.heappush(nums,calcVal)
            
        return -totalVal