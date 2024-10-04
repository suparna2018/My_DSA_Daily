# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimum-spanning-tree

from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        minHeap=[]
        vis=set()
        sum=0
        heapq.heappush(minHeap,(0,0))
        while(len(minHeap)>0):
            wt,node=heapq.heappop(minHeap)
            if node in vis:
                continue
            # add tthe node val to mst sum
            vis.add(node)
            sum+=wt
            for ele in adj[node]:
                Node,w=ele
                if Node not in vis:
                    heapq.heappush(minHeap,(w,Node))
        return sum