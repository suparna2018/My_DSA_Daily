"""
        0
      /  \
     1    1
    / \
   0   1
 /  \
1    1

Number of Island in Binary Tree.

"""
from typing import Self
from queue import Queue

class TreeNode:
    def __init__(self,left=None,val=0,right=None):
        self.left=None
        self.right=None
        self.val=val


class Solution:
    def findIsland(self,root):
        cnt=0
        def DFS(node,par):
            nonlocal cnt
            if node is None:
                return 
            if node.val==1 and par==0:
                cnt+=1
            DFS(node.left,node.val)
            DFS(node.right,node.val)

        DFS(root,0)
        print(f"Number of islands: {cnt}")
        print(cnt)
        return cnt
    
    def LevelOrder(self, root):
        def BFS(node):
            q = Queue()
            q.put(node)
            res = []
            while not q.empty():
                lvlVal = []
                lvlSize = q.qsize()
                for _ in range(lvlSize):
                    Node = q.get()
                    lvlVal.append(Node.val)
                    if Node.left is not None:
                        q.put(Node.left)
                    if Node.right is not None:
                        q.put(Node.right)
                res.append(lvlVal)
            for ele in res:
                print(ele)
        BFS(root)
        return

                    
# Tree construction
treeRoot = TreeNode(val=0)
treenode1 = TreeNode(val=1)
treenode2 = TreeNode(val=1)
treeRoot.left = treenode1
treeRoot.right = treenode2

treenode3 = TreeNode(val=0)
treenode4 = TreeNode(val=1)
treenode1.left = treenode3
treenode1.right = treenode4

treenode5 = TreeNode(val=1)
treenode6 = TreeNode(val=1)
treenode3.left = treenode5
treenode3.right = treenode6

# Solution execution
sol = Solution()
sol.LevelOrder(treeRoot)
sol.findIsland(treeRoot)





    

            