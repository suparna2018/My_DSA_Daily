"""
Problem statement
You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

Note:
You have an infinite number of elements of each type.
For example
If N=3 and X=7 and array elements are [1,2,3]. 
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 15
1 <= nums[i] <= (2^31) - 1
1 <= X <= 10000

All the elements of the “nums” array will be unique.
Time limit: 1 sec
Sample Input 1 :
2
3 7
1 2 3
1 0
1
Sample output 1 :
 3
 0
Explanation For Sample Output 1:
For the first test case,
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.

For the second test case,
Way 1 - You can take 3 elements  [1, 1, 1] as 1 + 1 + 1  = 3.
Way 2 - You can take 2 elements  [2, 1] as 2 + 1 = 3.
Here, you can see in Way 2 we have used 2 coins to reach the target sum of 7.
Hence the output is 2.
Sample Input 2 :
2
3 4
12 1 3
2 11
2 1
Sample output 2 :
2
6 
Python (3.5)
22212019181716151413111210967845312
            # not Take
            notTake=0+prev[target] 
            curr[target]=min(take,notTake)
        prev=curr[:]
    ans=prev[x]  
    if ans>=1e9:
        return -1
    return ans

"""

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def minimumElements(num: List[int], x: int) -> int:
    # def solve(ind,target,dp):
    #     if ind==0:
    #         if(target%num[0]==0):
    #             return target//num[0]
    #         return 1e9
    #     if (dp[ind][target]!=-1):
    #         return dp[ind][target]
    #     # take
    #     take=1e9
    #     if(num[ind]<=target):
    #         take=1+solve(ind,target-num[ind],dp)
    #     # not Take
    #     notTake=0+solve(ind-1,target,dp)
    #     dp[ind][target]=min(take,notTake)
    #     return dp[ind][target]

    # dp=[[0]*(x+1) for _ in range(len(num))]
    prev=[0]*(x+1)
    curr=[0]*(x+1)
    T=x+1
    for target in range(T):
        if(target%num[0]==0):
            prev[target]=target//num[0]
        else:
            prev[target]=1e9
                 
    for ind in range(1,len(num)):
        for target in range(x+1):
            # take
            take=1e9
            if(num[ind]<=target):
                take=1+curr[target-num[ind]]    
            # not Take
            notTake=0+prev[target] 
            curr[target]=min(take,notTake)
        prev=curr[:]
    ans=prev[x]  
    if ans>=1e9:
        return -1
    return ans