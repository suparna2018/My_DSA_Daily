from os import *
from sys import *
from collections import *
from math import *
from queue import Queue
from os import *
from sys import *
from collections import *
from math import *
from queue import Queue


def isBipartite(graph, vertices):
    adj=defaultdict(list)
    color=[-1]*vertices
    for u,v in graph:
        adj[u].append(v)
        adj[v].append(u)

    # print(graph,edges,vertices)
    # print(adj)
    def BFS(root):
        q=Queue()
        q.put(root)
        color[root]=1
        while(q.qsize()>0):
            node=q.get()
            for it in adj[node]:
                print(node ,it)
                if color[it]==-1:
                    color[it]=1-color[node]
                    q.put(it)
                else:
                    if color[it]==color[node]:
                        return False
        return True

    for _ in range(vertices):
        if color[_]==-1:
            # print(_)
            if not BFS(_):
                return False
    return True


       
adjacencyList=defaultdict(list)
adjacencyList=[[0,1],[0,2],[2,3],[2,5],[3,2],[3,4],[4,5]]

if (isBipartite(adjacencyList,6)):
    print("Yes,Bipartite")
else:
    print("No")



# 3
# 6 2
# 0 2
# 0 4
# 6 8
# 0 3
# 0 5
# 1 0
# 1 4
# 3 2
# 3 4
# 5 1
# 5 2
# 10 10
# 1 1
# 2 2
# 1 7
# 2 7
# 3 3
# 4 4
# 5 5
# 0 10
# 0 9
# 1 9