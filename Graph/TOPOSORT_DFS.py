# https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort

class Solution:
    def DFS(self,vis,adj,node,s):
        vis[node]=1
        for ele in adj[node]:
            if not vis[ele]:
                self.DFS(vis,adj,ele,s)
        s.append(node)
        
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        res=[]
        s=[]
        vis=[0]*V
        for i in range(V):
            if not vis[i]:
                self.DFS(vis,adj,i,s)
                
        while len(s):
            res.append(s.pop())
        # print(res)
        return res