# https://neetcode.io/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stores=[]
        for ele in stones:
            stores.append(-ele)

        heapq.heapify(stores)

        while len(stores)>1:
            stone1=heapq.heappop(stores)
            stone2=heapq.heappop(stores)

            res=abs(stone1-stone2)
            heapq.heappush(stores,-res)
        return -heapq.heappop(stores)