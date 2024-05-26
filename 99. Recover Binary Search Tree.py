from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root, li):
            if root is None:
                return li
            li = inorder(root.left, li)
            li.append(root)
            li = inorder(root.right, li)
            return li

        def helper(root):
            li = inorder(root, [])
            n = len(li)
            a = b = None
            
            for i in range(1, n):
                if li[i].val < li[i - 1].val:
                    a = li[i - 1]
                    break
            
            for i in range(n - 2, -1, -1):
                if li[i + 1].val < li[i].val:
                    b = li[i + 1]
                    break
            
            if a and b:
                a.val, b.val = b.val, a.val
        
        helper(root)

def test_recoverTree():
    def inorder_traversal(root):
        if root is None:
            return []
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
    
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)

    print("Before recovery: ", inorder_traversal(root))
    
    solution = Solution()
    solution.recoverTree(root)
    
    print("After recovery: ", inorder_traversal(root))

test_recoverTree()

