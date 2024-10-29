

from collections import defaultdict


def prerequisiteTask(dependency, n, m):
    adj=defaultdict(list)
    vis=[0]*(n+1)
    pathVis=[0]*(n+1)
    for u,v in dependency:
        adj[v].append(u)
    print(adj)
    def DetectCycle(src):
        vis[src]=1
        pathVis[src]=1
        for ele in adj[src]:
            # if not vis
            # print(ele)
            if vis[ele]==0:
                if DetectCycle(ele)==1:
                    return 1
                
            # if already vis
            elif pathVis[ele]==1:
                print("Cycle exists")
                return 1
                
        pathVis[src]=0
        return 0

    for _ in range(1,n):
        if vis[_]==0:
            if DetectCycle(_):
                return 1
    return 0



    
adjacencyList=defaultdict(list)

adjacencyList=[[1,2],[2,3],[3,1]]
# adjacencyList=[[1,2]]

# Solution=Solution()
if not prerequisiteTask(adjacencyList,3,3):
    print("Possible to Schedule")
else:
    print("Not Possible")