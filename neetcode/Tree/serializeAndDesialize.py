import queue
from typing import List,Optional
from collections import deque
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        self.res1=[]
        self.res2=[]
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            self.res1.append(root.val)
            inorder(root.right)

        def preorder(root):
            if root is None:
                return 
            self.res2.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        inorder(root)
        preorder(root)
        str1=','.join(str(ele) for ele in self.res1)
        str2=','.join(str(ele) for ele in self.res2)
        # print(str1)
        # print(str2)
        res=str1+"#"+str2
        # print(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        # print(data)
        if len(data)==1:
            return None
        ind=data.find('#')
        inorderStr =data[:ind]
        preorderStr=data[ind+1:]
        inorder=[int(ele) for ele in inorderStr.split(',')]
        preorder=[int(ele) for ele in preorderStr.split(',')]
        # print(inorder)
        # print(preorder)
        self.mp={}
        self.index=0
        for i,key in enumerate(inorder):
            self.mp[inorder[i]]=i
        # print(self.mp)

        def makeTree(start,end):
            if start>end:
                return None
            root=preorder[self.index]
            ind=self.mp[root]
            self.index+=1
            head=TreeNode(root)
            head.left=makeTree(start,ind-1)
            head.right=makeTree(ind+1,end)
            return head
        return makeTree(0,len(inorder)-1)
    
    
def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        currNode = queue.popleft()
        if values[i] is not None:
            currNode.left = TreeNode(values[i])
            queue.append(currNode.left)
        i += 1
        if i < len(values) and values[i] is not None:
            currNode.right = TreeNode(values[i])
            queue.append(currNode.right)
        i += 1
    return root

def print_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def GivePointer(root,val):
    if root is None:
        return
    if val<root.val:
        return GivePointer(root.left,val)
    elif val>root.val:
        return GivePointer(root.right,val)
    else:
        return root
    
# Test cases
@pytest.mark.parametrize("values", [
    [1, 2, 3, None, None, 4, 5],  # Example tree
    [1, None, 2, None, 3],        # Tree with only right children
    [1, 2, 3, 4, 5, 6, 7],        # Complete binary tree
    [1],                          # Single node
    []                            # Empty tree
])
def test_serializeDeserialize(values):
    solution = Codec()
    root = buildTree(values)
    seialized = Codec.serialize(root)
    deserialized=Codec.deserialize(seialized)
    result=print_tree(deserialized)
    assert result == values, f"Test failed for tree {values}. Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()
