

class Solution:
    def BellmanFord(self,V,source,edges):
        dist=[1e8]*(V)
        dist[source]=0
        for _ in range(V-1):
            for ele in edges:
                u,v,wt=ele
                # relax the edges
                if dist[u]!=1e8 and dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
        # nth time
        for ele in edges:
                u,v,wt=ele
                # relax the edges
                if dist[u]!=1e8 and dist[u]+wt<dist[v]:
                    return -1
        print(dist)
        return dist
    


solution=Solution()
edges=[[3,2,6],
       [2,4,3],
       [3,4,-2],
       [1,2,-2],
       [5,3,1],
       [0,1,5],
       [1,5,-3]
]

solution.BellmanFord(6,0,edges)



