


from collections import defaultdict
import heapq

class Solution:
    def Dijkstra(self,source,adj):
        pq=[] 
        dist=[1e9]*(len(adj))
        dist[source]=0
        heapq.heappush(pq,[0,source])
        while len(pq)>0:
            distantce,node=heapq.heappop(pq)
            for ele in adj[node]:
                neighbour,wt=ele
                if dist[node]+wt<dist[neighbour]:
                    dist[neighbour]=dist[node]+wt
                    heapq.heappush(pq,[dist[neighbour],neighbour])
        print(dist)
        return dist



adjacencyList=defaultdict(list)

adjacencyList={
    0:[[1,4],[2,4]],
    1:[[2,2],[0,4]],
    2:[[1,2],[5,6],[3,3],[0,4],[4,1]],
    3:[[2,3],[5,2]],
    4:[[2,1],[5,3]],
    5:[[2,6],[4,3],[3,2]]

}

Solution=Solution()
Solution.Dijkstra(0,adjacencyList)


