from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.mxHt=0
        def Depth(root):
            if root is None:
                return 1
            leftHeight=1
            rightHeight=1
            if root.left:
                leftHeight=Depth(root.left)
            if root.right:
                rightHeight=Depth(root.right)
            self.mxHt=max(leftHeight,rightHeight)
            # print(mxHt)
            return max(leftHeight,rightHeight)+1
        Depth(root)
        return self.mxHt 

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

# Test cases
def test_DiameterOfTree():
    solution = Solution()

    # Test case 1
    values = [4, 2, 7, 1, 3, 6, 9]
    root = buildTree(values)
    res = solution.maxDepth(root)
    expected_values = 3
    assert res == expected_values, f"Test case 1 failed, The depth output is {res}"
    print("Test case 1 passed")

test_DiameterOfTree()
