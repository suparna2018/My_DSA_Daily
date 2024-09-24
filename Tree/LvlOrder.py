import queue 
from typing import List, Optional
from collections import deque
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrder(root):
            if root is None:
                return []
            res=[]
            q=queue.Queue()
            q.put(root)
            while not q.empty():
                lvlSize=q.qsize()
                lvlVal=[]
                for i in range(lvlSize):
                    node=q.get()
                    lvlVal.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
                res.append(lvlVal)
            return res
        return levelOrder(root)
    
  
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
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),  # Tree: [3,9,20,None,None,15,7]
    ([1], [[1]]),  # Tree: [1]
    ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),  # Tree: [1,2,3,4,5,6,7]
    ([1, None, 2, None, 3], [[1], [2], [3]]),  # Tree: [1,None,2,None,3]
    ([], []),  # Empty tree
])
def test_levelOrder(values, expected):
    solution = Solution()
    root = buildTree(values)
    result = solution.levelOrder(root)
    assert result == expected, f"Test failed for tree {values}. Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()