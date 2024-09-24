# https://neetcode.io/problems/reverse-a-linked-list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        self.root=None
        def reverse(node):
            if node.next is None:
                self.root=node
                return None
            reverse(node.next)

            temp=node.next
            temp.next=node
            node.next=None
            return node
        reverse(head)  
        return self.root