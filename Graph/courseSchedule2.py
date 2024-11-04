"""
https://leetcode.com/problems/course-schedule-ii/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD

"""


from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            # Mark the current node as visited in both sets
            vis.add(node)
            pathvis.add(node)
            
            for neighbor in adj[node]:
                # If the neighbor has not been visited, do DFS on it
                if neighbor not in vis:
                    if dfs(neighbor) == 1:
                        return 1
                # If the neighbor is in the current path, a cycle is detected
                elif neighbor in pathvis:
                    return 1
            
            # Remove node from current path and add to result stack
            pathvis.remove(node)
            s.append(node)
            return 0

        # Initialization
        s = []
        vis = set()
        pathvis = set()
        adj = defaultdict(list)

        # Build the adjacency list
        for u, v in prerequisites:
            adj[v].append(u)

        # Perform DFS on each unvisited node
        for i in range(numCourses):
            if i not in vis:
                if dfs(i) == 1:
                    return []  # Return empty list if a cycle is detected

        return s[::-1]  # Return the topological order in reverse
      