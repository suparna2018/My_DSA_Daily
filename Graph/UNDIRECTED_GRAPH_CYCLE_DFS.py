# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph
from collections import defaultdict
from typing import List
class Solution:
    def DFS(self,V,adj,vis,src,parent):
        vis[src]=1
        for ele in adj[src]:
            if vis[ele]==0:
                if self.DFS(V,adj,vis,ele,src):
                    return True
            elif (parent!=ele):
                return True
        return False
        
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis=[0]*V
        for i in range(V):
            if vis[i]==0:
                if self.DFS(V,adj,vis,i,-1):
                    return True
        return False
	   
       
adjacencyList=defaultdict(list)
adjacencyList={
    0:[1,2],
    1:[0,3],
    2:[3,0,4],
    4:[3,2],
    3:[2,1,4],
}

Solution=Solution()
if Solution.isCycle(V=5,adj=adjacencyList):
    print("Cycle Exists")
else:
    print("No cycle is there")