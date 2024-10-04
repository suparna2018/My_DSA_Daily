# Disjoint set::::

class DisjointSet:
    def __init__(self,n) -> None:
        self.rank=[0]*(n+1)
        self.size=[0]*(n+1)
        self.parent=[0]*(n+1)
        for i in range(len(self.parent)):
            self.parent[i]=i
        
    def findParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]

    def UnionByRank(self,u,v):
        ulp_u=self.findParent(u)
        ulp_v=self.findParent(v)

        if ulp_u==ulp_v:
            return
        if self.rank[ulp_v]>self.rank[ulp_u]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1

    def UnionBySize(self,u,v):
        ulp_u=self.findParent(u)
        ulp_v=self.findParent(v)

        if ulp_u==ulp_v:
            return
        if self.size[ulp_v]<self.size[ulp_u]:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
        else:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]


# ds=DisjointSet(7)
# ds.UnionByRank(1, 2)
# ds.UnionByRank(2, 3)
# ds.UnionByRank(4, 5)
# ds.UnionByRank(6, 7)
# ds.UnionByRank(5, 6)
# if ds.findParent(3)!=ds.findParent(7):
#     print("Not Same")
# else:
#     print("Same")

# ds.UnionByRank(3, 6)
# if ds.findParent(3)!=ds.findParent(7):
#     print("Not Same")
# else:
#     print("Same")


ds=DisjointSet(7)
ds.UnionBySize(1, 2)
ds.UnionBySize(2, 3)
ds.UnionBySize(4, 5)
ds.UnionBySize(6, 7)
ds.UnionBySize(5, 6)
if ds.findParent(3)!=ds.findParent(7):
    print("Not Same")
else:
    print("Same")

ds.UnionBySize(3, 7)
if ds.findParent(3)!=ds.findParent(7):
    print("Not Same")
else:
    print("Same")
