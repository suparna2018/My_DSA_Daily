'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# print ('Hello World')

from queue import Queue
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q=Queue()
        q.put(root)
        prev=Node(-101)

        while not q.empty():
            lvl=[]
            dummy=prev
            for i in range(q.qsize()):
                popped=q.get()
                if popped.left:
                    q.put(popped.left)
                    dummy.next=popped.left
                    dummy=dummy.next
                if popped.right:
                    q.put(popped.right)
                    dummy.next=popped.right
                    dummy=dummy.next
        return root
def test_connect():
    # Specific test case: [1, 2, 3, 4, 5, 6, 7]
    # nodes = [1, 2, 3, 4, 5, 6, 7]
    
    # Building the tree manually for the specific test case
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    solution = Solution()
    connected_root = solution.connect(root)

    # Print the next pointers of each level
    def print_tree_next_pointers(root):
        while root:
            curr = root
            while curr:
                print(curr.val, end=" -> " if curr.next else " -> None\n")
                curr = curr.next
            # Move to the next level
            root = root.left if root.left else root.right

    print_tree_next_pointers(connected_root)

# Run the minimal test
test_connect()   
