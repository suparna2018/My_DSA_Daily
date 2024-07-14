from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(root1,root2):
            if (not root1 and not root2):
                return True
            elif (root1 and not root2) or (not root1 and root2) or (root1.val!=root2.val) :
                return False
            lft=same(root1.left,root2.left)
            rght=same(root1.right,root2.right)
            return lft and rght 
        return same(p,q)
    
def buildTree(values: List[ Optional[int]]) -> Optional[TreeNode]:
    if len(values)<1:
        return None
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    while i<len(values):
        currNode=queue.popleft()
        if values[i] is not None:
            currNode.left=TreeNode(values[i])
            queue.append(currNode.left)
            i+=1
        if i<len(values) and values[i] is not None:
            currNode.rightt=TreeNode(values[i])
            queue.append(currNode.rightt)
            i+=1
    return root

def printTree(root: Optional[TreeNode]) -> List[Optional[int]]:
    res=[]
    if root is None:
        return []
    queue=deque([root])
    while queue:
        node=queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    #Trim tariling Null
    while res and res[-1] is None:
        res.pop()
    return res

def TestCase():
    solution=Solution()
    input1=[1,0,2,3,5,5]
    input2=[1,0,2,3,4,5]
    root1=buildTree(input1)
    root2=buildTree(input2)

    tree1=printTree(root1)
    tree2=printTree(root2)
    # print(solution.isSameTree(root1,root2))
    assert solution.isSameTree(root1,root2), f"Test case 1 failed:  {tree1} != {tree2}"
    print("Test case 1 passed")

TestCase()