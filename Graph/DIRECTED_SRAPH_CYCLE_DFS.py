# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph    
#User function Template for python3
from typing import List

class Solution:
    def DFS(self,vis,pathvis,adj,src):
        vis[src]=1
        pathvis[src]=1
        for ele in adj[src]:
            # When the node is not visited
            if vis[ele]==0:
                if(self.DFS(vis,pathvis,adj,ele)==1):
                    return 1
            # when the node is visited already
            elif pathvis[ele]==1:
                return 1
                
        pathvis[src]=0
        return 0
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        vis=[0]*V
        pathvis=[0]*V
        for i in range(V):
            if vis[i]==0:
                if self.DFS(vis,pathvis,adj,i):
                    return 1
        return 0