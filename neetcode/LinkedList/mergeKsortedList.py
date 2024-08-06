# https://neetcode.io/problems/merge-k-sorted-linked-lists


import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        # Define less-than for ListNode to be used in heapq
        return self.val < other.val    

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap=[]
        for l in lists:
            if l:
                heapq.heappush(minHeap,l)

        dummy=ListNode(0)
        current=dummy

        while minHeap:
            smallestNode=heapq.heappop(minHeap)
            current.next=smallestNode
            current=current.next

            if smallestNode.next:
                heapq.heappush(minHeap,smallestNode.next)
        return dummy.next