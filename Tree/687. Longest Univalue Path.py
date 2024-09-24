
# print ('Hello World')
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        
        def helper(root, parent):
            if root is None:
                return 0
            left = helper(root.left, root)
            right = helper(root.right, root)
            self.maxi = max(self.maxi, left + right)
            if parent and root.val == parent.val:
                return max(left, right) + 1
            return 0
        
        helper(root, None)
        return self.maxi

# Minimal testing function for a specific test case
def test_longestUnivaluePath():
    # Specific test case: [5, 4, 5, 1, 1, None, 5]
    # Building the tree manually
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.longestUnivaluePath(root)
    print("Longest Univalue Path:", result)

# Run the minimal test
test_longestUnivaluePath()
