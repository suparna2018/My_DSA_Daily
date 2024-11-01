# https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=oizxjoit


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# BFS Approach

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q,clones=deque([node]),{node.val:Node(node.val,[])}    
        while q:
            curr=q.popleft()
            curr_clone=clones[curr.val]
            for neighbor in curr.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val]=Node(neighbor.val,[])
                    q.append(neighbor)
                curr_clone.neighbors.append(clones[neighbor.val])
                
        return clones[node.val]

# DFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, copyNode,vis):
            vis[copyNode.val]=copyNode
            for nghbr in node.neighbors:
                if nghbr.val not in vis:
                    newNode=Node(nghbr.val,[])
                    copyNode.neighbors.append(newNode)
                    dfs(nghbr,newNode,vis)
                else:
                    copyNode.neighbors.append(vis[nghbr.val])
        if not node:
            return None
        vis={}
        copy=Node(node.val,[])
        dfs(node,copy,vis)
        return copy