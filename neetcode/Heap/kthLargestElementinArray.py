# https://neetcode.io/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return heapq.heappop(nums)