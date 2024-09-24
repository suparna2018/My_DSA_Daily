from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inversion(root):
            if root is None:
                return
            inversion(root.left)
            inversion(root.right)
        
            temp=root.left
            root.left=root.right
            root.right=temp
        inversion(root)
        return root
    
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
def test_invertTree():
    solution = Solution()

    # Test case 1
    values = [4, 2, 7, 1, 3, 6, 9]
    root = buildTree(values)
    inverted_root = solution.invertTree(root)
    inverted_values = print_tree(inverted_root)
    expected_values = [4, 7, 2, 9, 6, 3, 1]
    assert inverted_values == expected_values, f"Test case 1 failed: {inverted_values} != {expected_values}"
    print("Test case 1 passed")

test_invertTree()





