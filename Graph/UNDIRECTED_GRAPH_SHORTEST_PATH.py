# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph-having-unit-distance


#User function Template for python3
from collections import defaultdict
from queue import Queue

class Solution:
    def shortestPath(self, edges, n, m, src):
        # adj matrix
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # DO the edge relaxation
        
        q=Queue()
        dist=[float('inf')]*n
        q.put(src)
        dist[src]=0
        while q.qsize()>0:
            node=q.get()
            for ele in adj[node]:
                if dist[ele]>dist[node]+1:
                    dist[ele]=dist[node]+1
                    q.put(ele)
        
        for i,ele in enumerate(dist):
            if ele==float('inf'):
                dist[i]=-1
                
        return dist
        
        
