from typing import List,Optional
from collections import deque
import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt=0
        mx=-float('inf')
        def gdNode(root,mx):
            if root is None:
                return   
            if root.val>=mx:
                print(root.val)
                mx=root.val
                self.cnt+=1
            if root.left:
                gdNode(root.left,mx)
            if root.right:
                gdNode(root.right,mx)
        gdNode(root,mx)
        return self.cnt
    
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
    
@pytest.mark.parametrize("values, expected", [
    ([3,1,4,3,None,1,5], 4),  # Tree: [3,1,4,3,None,1,5] -> Good nodes: 3, 4, 3, 5
    ([3,3,None,4,2], 3),       # Tree: [3,3,None,4,2] -> Good nodes: 3, 3, 4
    ([1], 1),                  # Tree: [1] -> Good nodes: 1
    ([2,None,4,10,8,None,None,4], 4),  # Tree: [2,None,4,10,8,None,None,4] -> Good nodes: 2, 4, 10, 8
    ([9,8,7,6,5,4,3], 1),      # Tree: [9,8,7,6,5,4,3] -> Good nodes: 9
])
def test_countGoodNodes(values, expected):
    solution = Solution()
    root = buildTree(values)
    result = solution.goodNodes(root)
    assert result == expected, f"Test failed for tree {values}. Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()
