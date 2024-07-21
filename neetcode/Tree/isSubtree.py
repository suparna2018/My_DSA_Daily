from typing import List,Optional
from collections import deque
import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:     
    def validTree(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is  None:
            return False
        if root.val!=subRoot.val:
            return False
        lv=self.validTree(root.left,subRoot.left)
        rv=self.validTree(root.right,subRoot.right)
        return lv and rv
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.validTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

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
    

@pytest.mark.parametrize("tree_values, subtree_values, expected", [
    ([3, 4, 5, 1, 2], [4, 1, 2], True),  # Subtree exists
    ([3, 4, 5, 1, 2], [4, None, 2], False),  # Subtree structure does not match
    ([1, 2, 3], [2], True),  # Subtree is a single node and exists
    ([1, 2, 3], [3], True),  # Subtree is a single node and exists
    ([1, 2], [3], False),  # Subtree does not exist
])
def test_isSubtree(tree_values, subtree_values, expected):
    solution = Solution()
    tree = buildTree(tree_values)
    subtree = buildTree(subtree_values)
    result = solution.isSubtree(tree, subtree)
    assert result == expected, f"Test failed for tree {tree_values} and subtree {subtree_values}. Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()