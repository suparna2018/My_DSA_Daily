"""
https://leetcode.com/problems/graph-valid-tree/description/?envType=problem-list-v2&envId=oizxjoit
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def BFS(adj,n,node):
            q=deque([[node,-1]])
            vis=set()
            vis.add(node)
            while len(q):
                node,par=q.popleft()
                for it in adj[node]:
                    if it not in vis:
                        vis.add(it)
                        q.append([it,node])
                    else:
                        if it!=par:
                            return False
            if len(vis)==n:
                return True
            else:
                return False

        adj=defaultdict(list)
        for ele in edges:
            u,v=ele
            adj[u].append(v)
            adj[v].append(u)

        return BFS(adj,n,0)        