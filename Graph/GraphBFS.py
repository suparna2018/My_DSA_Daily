# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bfs_of_graph

#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q=Queue()
        q.put(0)
        vis=[0]*V
        res=[]
        vis[0]=1
        while q.qsize():
            node=q.get()
            res.append(node)
            for ele in adj[node]:
                if vis[ele]==0:
                    vis[ele]=1
                    q.put(ele)
        return res
        
        
