# https://neetcode.io/problems/remove-node-from-end-of-linked-list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def lenghtLL(head):
            cnt=0
            while head:
                head=head.next
                cnt+=1
            return cnt
        dummy=ListNode()
        dummy.next=head
        print(lenghtLL(head))
        root=dummy
        target=lenghtLL(head)-n
        x=0
        while root:
            if x==target:
                root.next=root.next.next
                break
            root=root.next
            x+=1
            
        return dummy.next

        