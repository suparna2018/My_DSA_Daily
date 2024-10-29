# https://www.naukri.com/code360/problems/shortest-subarray-with-sum-at-least-k_975374?interviewProblemRedirection=true&page=2&company%5B%5D=PayPal&company%5B%5D=PayPal%20India%20Pvt%20Lt&difficulty%5B%5D=Medium&difficulty%5B%5D=Hard&difficulty%5B%5D=Ninja&sort_entity=company_count&sort_order=DESC&leftPanelTabValue=SOLUTION


# def shortestSubarrayWithSumK(arr, k):
#     ans=sys.maxsize
#     n=len(arr)
#     for i in range(n):
#         sum = 0
        
#         # Iterate through the array and find subarrays starting at index i
#         for j in range(i, n):
#             sum += arr[j]  # Add arr[j] instead of arr[i]
            
#             # If the sum becomes greater than or equal to k
#             if sum >= k:
#                 ans = min(ans, j - i + 1)  # Calculate subarray length
#                 break
#     if ans==sys.maxsize:
#         return -1
#     else:
#         return ans
    


# ----------------------------------------------------------------------------------------------------------


'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where 'N' is the number of elements in the given array/list.
'''

import sys
from collections import deque
    
def shortestSubarrayWithSumK(arr, k):
    
    n = len(arr)
    
    # For storing prefix sums.
    prefixSum = []
    
    prefixSum.append(0)
    
    # Iterate through the array/list to calculate prefix sums.
    for i in range(1, n + 1):
        
        prefixSum.append(prefixSum[i - 1] + arr[i - 1])
        
    # For storing the length of the shortest subarray with sum >= K.
    subarraySumK = sys.maxsize
    
    # Double ended queue for maintaing increasing order of prefix sums.
    increasingPrefix = deque()
    
    for i in range(n + 1):
        
        # Pop elements from the back of the queue.
        while len(increasingPrefix) > 0 and prefixSum[i] <= prefixSum[increasingPrefix[-1]]:
            
            increasingPrefix.pop()
            
        # Pop elements from the front of the queue.
        while len(increasingPrefix) > 0 and prefixSum[i] >= prefixSum[increasingPrefix[0]] + k:
            
            # Update the value of subarraySumK.
            subarraySumK = min(subarraySumK, i - increasingPrefix[0])
            
            increasingPrefix.popleft()
            
        # Insert the current index at the back of the queue.
        increasingPrefix.append(i)
        
    # Return -1 if no subarray has sum greater than or equal to K.
    if subarraySumK == sys.maxsize:
        
        return -1
        
    # Else return the length of the shortest subarray with sum greater than or equal to K.
    else:
        
        return subarraySumK
