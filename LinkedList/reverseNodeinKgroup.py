# https://neetcode.io/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        def reverseNode(head, k):
            prev, current = None, head
            while k:
                newNode = current.next
                current.next = prev
                prev = current
                current = newNode
                k -= 1
            return prev
        len=0
        ptr=head
        while len<k and ptr:
              ptr=ptr.next
              len+=1
               
        if len==k:
            reverseHead=reverseNode(head,k)

            head.next= self.reverseKGroup(ptr,k)
            return reverseHead
        return head