"""
Problem statement
You are given an array 'arr' containing 'n' non-negative integers.



Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.



You just need to find the minimum absolute difference considering any valid division of the array elements.



Note:

1. Each array element should belong to exactly one of the subsets.

2. Subsets need not always be contiguous.
For example, for the array : [1, 2, 3], some of the possible divisions are 
   a) {1,2} and {3}
   b) {1,3} and {2}.

3. Subset-sum is the sum of all the elements in that subset. 
Example:
Input: 'n' = 5, 'arr' = [3, 1, 5, 2, 8].

Ouput: 1

Explanation: We can partition the given array into {3, 1, 5} and {2, 8}. 
This will give us the minimum possible absolute difference i.e. (10 - 9 = 1).
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
4
1 2 3 4
Sample Output 1:
0
Explanation for sample input 1:
We can partition the given array into {2,3} and {1,4}.
This will give us the minimum possible absolute difference i.e. (5 - 5 = 0) in this case.
Sample Input 2:
3
8 6 5
Sample Output 2:
3
Explanation for sample input 2:
We can partition the given array into {8} and {6,5}. 
This will give us the minimum possible absolute difference i.e. (11 - 8 = 3).
Expected time complexity:
The expected time complexity is O(n * 𝚺 'arr'[i]), where 𝚺 'arr'[i] denotes the sum of all elements in 'arr'.
Constraints:
1 <= 'n' <= 10^3
0 <= 'arr'[i] <= 10^3
0 <= 𝚺 'arr'[i] <= 10^4, 

where 𝚺 'arr'[i] denotes the sum of all elements in 'arr'.

Time Limit: 1sec
"""

from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totSum = sum(arr)
    n=len(arr)
        # Initialize a DP table to store subset sum information.
    dp = [[False for i in range(totSum + 1)] for j in range(n)]

        # Initialize the base cases for the DP table.
    for i in range(n):
        dp[i][0] = True

        # Handle the base case for the first element in the array.
    if arr[0] <= totSum:
        dp[0][arr[0]] = True

        # Fill in the DP table using dynamic programming.
    for ind in range(1, n):
        for target in range(1, totSum + 1):
                # If the current element is not taken, the result is the same as the previous row.
            notTaken = dp[ind - 1][target]

                # If the current element is taken, subtract its value from the target and check the previous row.
            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]

                # Update the DP table with the result of taking or not taking the current element.
            dp[ind][target] = notTaken or taken

            # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

            # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini 