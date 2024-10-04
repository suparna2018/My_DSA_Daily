
import heapq

class DisjointSet:
    def __init__(self,n) -> None:
        self.rank=[0]*(n+1)
        self.par=[0]*(n+1)
        for i in range(len(self.par)):
            self.par[i]=i

    def findParent(self,node):
        if node==self.par[node]:
            return node
        self.par[node]=self.findParent(self.par[node])


    def unionByRank(self,u,v):
        ulp_u=self.findParent(u)
        ulp_v=self.findParent(v)
        if ulp_u==ulp_v:
            return
        if self.rank[ulp_u]>self.rank[ulp_v]:
            self.par[ulp_v]=ulp_u
        elif self.rank[ulp_v]>self.rank[ulp_u]:
            self.par[ulp_u]=ulp_v
        else:
            self.par[ulp_u]=ulp_v
            self.rank[ulp_v]+=1

class Solution:
    def kruskal(self,V,adj):
        mstWt=0
        pq=[]
        for ele in adj:
            u,v,wt=ele
            heapq.heappush(pq,[wt,u,v])

        ds=DisjointSet(V)
        while len(pq)>0:
            w,u,v=heapq.heappop(pq)
            if ds.findParent(u)!=ds.findParent(v):
                mstWt+=w
                ds.unionByRank(u,v)
        print(mstWt)

Solution=Solution()
V=3
adj=[]
adj.append([0,1,5])
adj.append([1,2,3])
adj.append([0,2,1])

Solution.kruskal(V,adj)


