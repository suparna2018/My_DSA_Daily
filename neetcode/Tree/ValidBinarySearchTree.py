from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root,left,right):
            if root is None:
                return True
            if not left<root.val<right:
                return False
            else:
                return isValid(root.left,left,root.val) and isValid(root.right,root.val,right)
            
        return isValid(root,-float('inf'),float('inf'))
    
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
    input1=[]
    input2=[]
    root1=buildTree(input1)
    root2=buildTree(input2)

    tree1=printTree(root1)
    tree2=printTree(root2)
    # print(solution.isSameTree(root1,root2))
    assert solution.isSameTree(root1,root2), f"Test case 1 failed:  {tree1} != {tree2}"
    print("Test case 1 passed")

TestCase()
    
