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

# Leetcode Merge k sorted List 
# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM%2CHARD

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# import heapq
# from typing import List, Optional

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         heap = []
#         dummy = ListNode(0)
#         curr = dummy
        
#         # Populate the heap with initial nodes from each list
#         for idx, ele in enumerate(lists):
#             if ele:
#                 # Push the tuple (value, index, node) to avoid comparison issues
#                 heapq.heappush(heap, (ele.val, idx, ele))
        
#         while heap:
#             # Pop the smallest item from the heap
#             nodeVal, idx, node = heapq.heappop(heap)
#             curr.next = node
#             curr = curr.next  # Move current pointer to next node
            
#             # If there’s a next node, push it into the heap with the same index
#             if node.next:
#                 heapq.heappush(heap, (node.next.val, idx, node.next))
        
#         return dummy.next