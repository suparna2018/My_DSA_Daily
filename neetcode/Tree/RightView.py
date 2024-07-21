import queue
from typing import List,Optional
from collections import deque
import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
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

        res=levelOrder(root)
        for ele in res:
            # ele.reverse()
            ans.append(ele[-1])
        return ans
    
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
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),  # Tree: [1,2,3,None,5,None,4] -> Right view: 1, 3, 4
    ([1], [1]),  # Tree: [1] -> Right view: 1
    ([1, None, 2, None, 3], [1, 2, 3]),  # Tree: [1,None,2,None,3] -> Right view: 1, 2, 3
    ([1, 2, 3, 4, 5, None, 6], [1, 3, 6]),  # Tree: [1,2,3,4,5,None,6] -> Right view: 1, 3, 6
    ([], []),  # Empty tree
])
def test_rightSideView(values, expected):
    solution = Solution()
    root = buildTree(values)
    result = solution.rightSideView(root)
    assert result == expected, f"Test failed for tree {values}. Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()