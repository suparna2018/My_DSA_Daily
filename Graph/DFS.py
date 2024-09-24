# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=dfs_of_graph


#User function Template for python3

class Solution:
    def DFS(self,V,adj,node,vis,res):
        vis[node]=1
        res.append(node)
        for ele in adj[node]:
            if vis[ele]==0:
                self.DFS(V,adj,ele,vis,res)
        return res
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        vis=[0]*V
        vis[0]=1
        res=self.DFS(V,adj,0,vis,[])
        return res
        
