
# https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=strongly-connected-components-kosarajus-algo


from collections import defaultdict


def DFS(node, adj,vis,st):
    vis.add(node)
    for neighbour in adj[node]:
        if neighbour not in vis:
            DFS(neighbour,adj,vis,st)
    st.append(node)
        
class Solution:
   
        
    def kosaraju(self, V, adj):
        vis=set()
        sec=0
        st=[]
        for i in range(len(adj)):
            if i not in vis:
                DFS(i,adj,vis,st)
        # step 2
        adjR=defaultdict(list)
        for i in range(len(adj)):
            for ele in adj[i]:
                adjR[ele].append(i)
        # DFS 3
        vis=set()
        while len(st)>0:
            node=st[-1]
            st.pop()
            if node not in vis:
                sec+=1
                DFS(node,adjR,vis,[])
        return sec