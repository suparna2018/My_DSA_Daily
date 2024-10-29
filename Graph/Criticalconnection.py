



# https://leetcode.com/problems/critical-connections-in-a-network/description/




class Solution:
    def __init__(self):
        self.timer=1
        self.bridges=[]

    def dfs(self,node,par,adj,time,low,vis):
        vis.add(node)
        time[node]=low[node]=self.timer
        self.timer+=1
        for it in adj[node]:
            if(it==par):continue
            if it not in vis:
                self.dfs(it,node,adj,time,low,vis)
                low[node]=min(low[node],low[it])
                if low[it]>time[node]:
                    self.bridges.append([node,it])
            else:
                low[node]=min(low[node],low[it])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj=defaultdict(list)
        for ele in connections:
            u,v=ele
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        time=[0]*(n+1)
        low=[0]*(n+1)
        self.dfs(0,-1,adj,time,low,vis)
        return self.bridges

