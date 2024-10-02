# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=direct-acyclic-graph

#User function Template for python3
from collections import defaultdict
from typing import List

class Solution:
    def topoSort(self,adj,N):
        def dfs(Adj,vis,st,src):
            vis[src]=1
            for neighbour,wt in adj[src]:
                if vis[neighbour]==0:
                    dfs(Adj,vis,st,neighbour)
            st.append(src)
        st=[]
        vis=[0]*N
        dfs(adj,vis,st,0)
        return st[::-1]
        
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        # adjacency list formation
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
        
        # print(adj)
        # TopoSort
        st=self.topoSort(adj,n)
        #  edge relaxation
        dist=[1e9]*n
        dist[0]=0
        for i in st:
            for neighbour,wt in adj[i]:
                if (dist[i]+ wt < dist[neighbour]):
                    dist[neighbour]=dist[i] + wt
        
        for i in range(n):
            if dist[i]==1e9:
                dist[i]=-1
        
        # print(dist)
        return dist
            
        
        
        
        
        
