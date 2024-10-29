'''
Given an array arr[] of size N. In each operation, pick an array element X and remove all array elements in the range [X – 1, X + 1]. The task is to find the maximum number of steps required such that no coins left in the array.

Examples:


Input: coins [] = {5, 1, 3, 2, 6, 7, 4} 
Output: 4 
Explanation: 
Picking the coin coins[1] modifies the array arr[] = {5, 3, 6, 7, 4}. 
Picking the coin coins[1] modifies the array arr[] = {5, 6, 7} 
Picking the coin coins[0] modifies the array arr[] = {7} 
Picking the coin coins[0] modifies the array arr[] = {}. Therefore, the required output is 4.


Input: coins [] = {6, 7, 5, 1} 
Output: 3

'''