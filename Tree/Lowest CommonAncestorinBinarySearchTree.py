from typing import List,Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def LCS(root):
            if root is None:
                return None
            if(root.val<p.val and root.val<q.val):
                return LCS(root.right)
            elif(root.val>p.val and root.val>q.val):
                return LCS(root.left)
            else:
                return root
        return LCS(root)

def buildTree(values: List[Optional[int]])-> Optional[TreeNode]:
    if not values:
        return None
    root=TreeNode(values[0])
    queue=deque([root])

    i=1
    while i<len(values):
        currentNode=queue.popleft()

        if values[i] is not None:
            currentNode.left=TreeNode(values[i])
            queue.append(currentNode.left)
            i+=1
        if i<len(values) and values[i] is not None:
            currentNode.right=TreeNode(values[i])
            queue.append(currentNode.right)
            i+=1
        
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
def test_LCA():
    solution = Solution()

    # Test case 1
    values = [5,3,8,1,4,7,9,None,2]
    root = buildTree(values)
    print_tree(root)
    p=GivePointer(root,3)
    print(p.val)
    q=GivePointer(root,8)
    print(q.val)
    res = solution.lowestCommonAncestor(root,p,q)
    print(res.val)
    expected_values = 5
    assert res.val == expected_values, f"Test case 1 failed ,function result is {res.val}"
    print("Test case 1 passed")

test_LCA()
