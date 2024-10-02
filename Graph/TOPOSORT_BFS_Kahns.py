# https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort


from queue import Queue

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree=[0]*V
        for i in range(V):
            for ele in adj[i]:
                indegree[ele]+=1
        
        q=Queue()
        for i in range(V):
            if indegree[i]==0:
                q.put(i)
        
        # BFS
        topo=[]
        while q.qsize():
            node=q.get()
            topo.append(node)
            for ele in adj[node]:
                indegree[ele]-=1
                if indegree[ele]==0:
                    q.put(ele)
        return topo
        
                
        
        
        

