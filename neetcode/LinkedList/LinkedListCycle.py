# https://neetcode.io/problems/linked-list-cycle-detection

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slo=head
        fast=head
        while slo.next and fast.next.next:
            slo=slo.next
            fast=fast.next.next
            if slo==fast:
                return True
        return False