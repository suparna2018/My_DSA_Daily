# https://neetcode.io/problems/kth-largest-integer-in-a-stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k= nums,k
        heapq.heapify(self.minHeap)
        while k<len(self.minHeap):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        