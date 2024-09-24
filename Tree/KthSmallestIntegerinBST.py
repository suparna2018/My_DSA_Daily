from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=[]
        def inOrder(root):
            if root is None:
                return
            if len(self.res)<=k:
                inOrder(root.left)
                self.res.append(root.val)
                inOrder(root.right)
        inOrder(root)
        # print(self.res)
        return self.res[k-1]
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
def test_KthSmallest():
    solution = Solution()

    # Test case 1
    values = [4,5,6,7,12,18,19]
    root = buildTree(values)
    res = solution. kthSmallest(root,2)
    expected_values = 5
    assert res == expected_values, "Test case 1 failed"
    print("Test case 1 passed")

test_KthSmallest()
