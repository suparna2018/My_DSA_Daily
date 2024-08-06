# https://neetcode.io/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        extra=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0

            value=(x+y+extra)
            
            newNode=ListNode(value%10)
            extra=value//10

            curr.next=newNode
            curr=curr.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        if extra==1:
            newNode.next=ListNode(extra)

        return dummy.next
        
        