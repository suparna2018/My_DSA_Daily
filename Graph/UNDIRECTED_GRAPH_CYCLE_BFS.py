# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph

from collections import defaultdict
from queue import Queue

class Solution:
    def UndirectedGraphCycle(self,source,adj):
        vis=set()
        def BFS(src,adj):
            # nonlocal vis

            q=Queue()
            q.put([src,-1])
            vis.add(src)
            while not q.empty():
                node,par=q.get()
                print(node)
                for ele in adj[node]:
                    if ele not in vis:
                        vis.add(ele)
                        q.put([ele,node])
                    # node already visited
                    elif (par!=ele):
                        return True
            return False
        
        for ele in adj:
            if ele not in vis:
                if BFS(ele,adj):
                    return True
                
        return False
    
adjacencyList=defaultdict(list)

adjacencyList={
    0:[1],
    1:[2,3],
    2:[5,1],
    3:[],
    5:[0],
}

Solution=Solution()
if Solution.UndirectedGraphCycle(source=0,adj=adjacencyList):
    print("Cycle Exists")
else:
    print("No cycle is there")