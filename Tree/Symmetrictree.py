# https://www.naukri.com/code360/problems/symmetric-tree_981177?interviewProblemRedirection=true&company%5B%5D=Arcesium&difficulty%5B%5D=Medium,Hard,Ninja&sort_entity=recents&sort_order=DESC

# Following is the structure of Tree Node:
# Following is the structure of Tree Node:
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isSymmetric(root: TreeNode) -> bool:
    def mirror(root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.data==root2.data:
            return mirror(root1.left,root2.right) and mirror(root1.right,root2.left)
        else:
            return False
    return mirror(root.left,root.right)

        
        



# Example usage:
# Constructing a symmetric tree:
#        1
#      /   \
#     2     2
#    / \   / \
#   3   4 4   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Check if the tree is symmetric
if isSymmetric(root):
    print("Yes")  # Output: True
else:
    print("No")
