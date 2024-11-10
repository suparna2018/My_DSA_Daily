"""
https://leetcode.com/problems/alien-dictionary/description/?envType=problem-list-v2&envId=oizxjoit&status=TO_DO&difficulty=MEDIUM%2CHARD
"""



from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def topoSort(adj, indegree, allChrs):
            # BFS (Kahn's Algorithm)
            q = deque()
            for char in allChrs:
                if indegree[char] == 0:
                    q.append(char)
            
            topo = []
            while q:
                node = q.popleft()
                topo.append(node)
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            # If the topo list doesn't contain all the unique characters, return ""
            if len(topo) != len(allChrs):
                return ""
            return "".join(topo)

        adj = defaultdict(set)  # adjacency list
        indegree = defaultdict(int)  # to store indegree of each node (character)
        allChrs = set("".join(words))  # all unique characters in the words

        # Check for invalid cases where a word is a prefix of another word
        for i in range(len(words) - 1):
            s1, s2 = words[i], words[i + 1]
            if len(s1) > len(s2) and s1[:len(s2)] == s2:
                # If s1 is longer and a prefix of s2, it's an invalid order
                return ""

        # Build the graph (adjacency list) and indegree map
        for i in range(len(words) - 1):
            s1, s2 = words[i], words[i + 1]
            for j in range(min(len(s1), len(s2))):
                if s1[j] != s2[j]:
                    if s2[j] not in adj[s1[j]]:
                        adj[s1[j]].add(s2[j])  # add edge from s1[j] -> s2[j]
                        indegree[s2[j]] += 1  # increment indegree of s2[j]
                    break

        # Initialize indegree of nodes that have no incoming edges
        for char in allChrs:
            if char not in indegree:
                indegree[char] = 0
        
        return topoSort(adj, indegree, allChrs)
