from typing import List,Optional
from collections import deque
import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal= -float('inf')
        def dfs(root):
            if root is None:
                return 0
            lv=max(dfs(root.left),0)
            rv=max(dfs(root.right),0)
            self.maxVal=max(self.maxVal,lv+rv+root.val)
            print(self.maxVal)
            return max(lv,rv)+root.val


        dfs(root)
        return self.maxVal
  
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
@pytest.mark.parametrize("values, expected", [
    ([-15, 10, 20, None, None, 15, 5, -5], 40),
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42),
    ([], -float('inf')),
    ([1], 1)
])

def test_maxPathSum(values, expected):
    solution = Solution()
    root = buildTree(values)
    result = solution.maxPathSum(root)
    assert result == expected, f"Test failed for tree {values}. Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()