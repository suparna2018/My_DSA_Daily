"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM%2CHARD&status=TO_DO
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def     dfs(vis,root):
            vis.add(root)
            for it in adj[root]:
                if it not in vis:
                    dfs(vis,it)
        adj=defaultdict(list)
        for ele in edges:
            u,v=ele
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        cnt=0
        for i in range(n):
            if i not in vis:
                cnt+=1
                dfs(vis,i)
        
        return cnt  