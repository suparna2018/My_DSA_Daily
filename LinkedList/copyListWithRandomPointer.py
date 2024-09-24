# https://neetcode.io/problems/copy-linked-list-with-random-pointer

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr=head
        while curr:
            new_node=Node(curr.val)
            new_node.next=curr.next
            curr.next=new_node
            # if curr.random:
            #     new_node.random=curr.random.next
            curr=new_node.next

        curr=head    
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next

        # link the new nodes
        curr=head
        copyHead=head.next
        while curr:
            copy=curr.next
            curr.next=copy.next
            if copy.next:
                copy.next=copy.next.next
            curr=curr.next

        return copyHead
