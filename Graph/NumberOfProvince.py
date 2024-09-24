# https://www.geeksforgeeks.org/problems/number-of-provinces/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number_of_provinces

#User function Template for python3
from queue import Queue
from collections import defaultdict

class Solution:
    def numProvinces(self, adj, V):
        def adjMatrixToList(adj, adjList):
            n=len(adj)
            m=len(adj[0])
            for i in range(n):
                for j in range(m):
                    if adj[i][j]==1:
                        adjList[i].append(j)
            # return adjList
        
        def BFS(adjList,src,vis):
            q=Queue()
            q.put(src)
            vis[src]=1
            vec=[]
            # vis=[0]*len(adj)
            while q.qsize():
                node=q.get()
                vec.append(node)
                for ele in adjList[node]:
                    # print(node,ele)
                    if vis[ele]!=1:
                        q.put(ele)
                        vis[ele]=1
            # print(vec)
            return vec
            
        adjList=defaultdict(list)
        adjMatrixToList(adj, adjList)
        # print(adjList)
        cnt=0
        res=[]
        vis=[0]*len(adj)
        for i in range(len(adj)):
            if vis[i]==0:
                island=BFS(adjList,i,vis)
                cnt+=1
                res.append(island)
        # print(res)
        return cnt