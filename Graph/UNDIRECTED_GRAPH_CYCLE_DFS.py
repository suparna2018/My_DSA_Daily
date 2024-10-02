# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph



from typing import List
class Solution:
    def DFS(self,V,adj,vis,src,parent):
        vis[src]=1
        for ele in adj[src]:
            if vis[ele]==0:
                if self.DFS(v,adj,vis,ele,src):
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
	   
	            
	            
	        
#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends