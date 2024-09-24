# https://neetcode.io/problems/reorder-linked-list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find Mid
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # reverse the 2nd half
        prev,curr=None, slow.next
        slow.next=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        # Merge the parts
        first,second=head,prev
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
