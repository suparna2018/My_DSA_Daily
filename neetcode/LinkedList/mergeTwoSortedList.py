# https://neetcode.io/problems/merge-two-sorted-linked-lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2

        dummy=ListNode()
        current=dummy

        while l1 and l2:
            if l1.val<=l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next

        if l1:
            current.next=l1
        elif l2:
            current.next=l2

        return dummy.next       