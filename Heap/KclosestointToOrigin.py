# https://neetcode.io/problems/k-closest-points-to-origin

import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mp=defaultdict(list)
        def Distance(x,y):
            return math.sqrt(x*x+y*y)
        store=[]
        heapq.heapify(store)
        for ele in points:
            dist=Distance(ele[0], ele[1])
            heapq.heappush(store, [dist,[ele[0], ele[1]]] )
        res=[]

        while k:
            nodePair=heapq.heappop(store)
            res.append(nodePair[1])
            k-=1

        return res