# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        curr = dummy
        
        # Populate the heap with initial nodes from each list
        for idx, ele in enumerate(lists):
            if ele:
                # Push the tuple (value, index, node) to avoid comparison issues
                heapq.heappush(heap, (ele.val, idx, ele))
        
        while heap:
            # Pop the smallest item from the heap
            nodeVal, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next  # Move current pointer to next node
            
            # If there’s a next node, push it into the heap with the same index
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next