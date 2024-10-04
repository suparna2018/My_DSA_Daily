# https://www.geeksforgeeks.org/problems/articulation-point-1/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=articulation-point

#User function Template for python3

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def DFS(node, par, adj, vis, time, low, mark, timer):
    vis.add(node)
    time[node] = low[node] = timer[0]
    timer[0] += 1
    child = 0
    for it in adj[node]:
        if it == par:
            continue
        if it not in vis:
            child += 1
            DFS(it, node, adj, vis, time, low, mark, timer)
            low[node] = min(low[node], low[it])
            # Condition to check if the node is an articulation point
            if low[it] >= time[node] and par != -1:
                mark[node] = 1
        else:
            low[node] = min(low[node], time[it])
    
    if child > 1 and par == -1:
        mark[node] = 1

class Solution:
    def articulationPoints(self, V, adj):
        vis = set()
        time = [0] * V
        low = [0] * V
        mark = [0] * V
        ans = []
        timer = [0]
        DFS(0, -1, adj, vis, time, low, mark, timer) 
        for i in range(len(mark)):
            if mark[i] == 1:
                ans.append(i)
                
        return ans if len(ans) > 0 else [-1]

                

