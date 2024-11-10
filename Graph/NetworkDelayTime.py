"""
https://leetcode.com/problems/network-delay-time/description/

"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Use dijhstras
        pq=[(0,k)]
        adj=defaultdict(list)
        for ele in times:
            u,v,t=ele
            adj[u].append([v,t])

        dist=[1e9]*(n+1)
        dist[k]=0
        
        while pq:
            d,node=heapq.heappop(pq)
            for neighbour,_ in adj[node]:
                if dist[node]+_<dist[neighbour]:
                    dist[neighbour]= dist[node]+_
                    heapq.heappush(pq,([dist[node]+_,neighbour]))

        maxDist=max(dist[1:])
        return maxDist if maxDist<1e9 else -1